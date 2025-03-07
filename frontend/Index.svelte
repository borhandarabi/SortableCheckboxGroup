<!-- svelte-ignore unused-export-let -->
<svelte:options immutable={true} />

<script lang="ts">
	import type { Gradio, SelectData } from "@gradio/utils";
	import { Block, BlockTitle } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";
	import { onMount } from "svelte";

	interface Translation {
		sortablecheckboxgroup: {
			[key: string]: string;
		};
	}

	interface Translations {
		[lang: string]: Translation;
	}

	interface ExtendedGradio extends Gradio<{
		change: never;
		select: SelectData;
		input: never;
		clear_status: LoadingStatus;
	}> {
		language?: string;
		config?: {
			translations?: Translations;
		};
		autoscroll: boolean;
		i18n: any;
	}

	export let gradio: ExtendedGradio;
	
	// Main props used in the component
	export let value: (string | number)[] = [];
	export let choices: [string, string | number][];
	export let loading_status: LoadingStatus;
	export let interactive = true;
	export let sortable = false;
	export let show_order = false;
	export let old_value = [...value];
	
	// Other props are managed dynamically
	$: ({
		target,
		type,
		key,
		name,
		_selectable,
		attached_events,
		server,
		theme_mode,
		queue_position,
		queue_size,
		status,
		elem_id,
		elem_classes,
		visible,
		container,
		scale,
		min_width,
		label,
		info,
		show_label,
		root
	} = $$props);

	export let translations: Translations = {};
	
	// Check if translations are properly set
	function checkTranslations() {
		if (!translations || Object.keys(translations).length === 0) {
			translations = {
				"en": {
					"sortablecheckboxgroup": {
						"priority_order": "Priority Order",
						"move_up": "Move Up",
						"move_down": "Move Down",
						"keyboard_usage_guide": "Use arrow keys to move, Enter or Space to select/deselect, Escape to cancel",
						"moving": "Currently moving",
						"keyboard_instructions": "Keyboard instructions",
						"arrow_keys_guide": "Use arrow keys to move items",
						"enter_space_guide": "Use Enter or Space to select and move items",
						"escape_guide": "Use Escape to cancel selection",
						"sortable_items_list": "Sortable items list",
						"show_order": "Show priority order",
						"hide_order": "Hide priority order"
					}
				},
				"fa": {
					"sortablecheckboxgroup": {
						"priority_order": "ترتیب اولویت",
						"move_up": "انتقال به بالا",
						"move_down": "انتقال به پایین",
						"keyboard_usage_guide": "از کلیدهای جهت‌دار برای جابجایی، Enter یا Space برای انتخاب/لغو انتخاب و Escape برای لغو استفاده کنید",
						"moving": "در حال جابجایی",
						"keyboard_instructions": "راهنمای استفاده از صفحه کلید",
						"arrow_keys_guide": "از کلیدهای جهت‌دار برای جابجایی آیتم‌ها استفاده کنید",
						"enter_space_guide": "از کلیدهای Enter یا Space برای انتخاب و جابجایی آیتم‌ها استفاده کنید",
						"escape_guide": "از کلید Escape برای لغو انتخاب استفاده کنید",
						"sortable_items_list": "لیست آیتم‌های قابل مرتب‌سازی",
						"show_order": "نمایش ترتیب اولویت",
						"hide_order": "پنهان کردن ترتیب اولویت"
					}
				}
			};
		}
	}

	// Get current language
	function getCurrentLanguage(): string {
		if (gradio && gradio.language) {
			return gradio.language;
		}
		return "en";
	}

	function getTranslation(key: string): string {
		const lang = getCurrentLanguage();
		if (translations && translations[lang]?.sortablecheckboxgroup?.[key]) {
			return translations[lang].sortablecheckboxgroup[key];
		}
		if (translations?.en?.sortablecheckboxgroup?.[key]) {
			return translations.en.sortablecheckboxgroup[key];
		}
		return key;
	}

	// Set translations from backend
	function setTranslationsFromBackend() {
		if (gradio?.config?.translations) {
			translations = gradio.config.translations;
		}
	}

	function toggle_choice(choice: string | number): void {
		if (value.includes(choice)) {
			value = value.filter((v) => v !== choice);
		} else {
			const newValue = [...value, choice];
			value = newValue;
		}
		gradio.dispatch("input");
	}

	let draggedItemIndex: number | null = null;
	let isDragging = false;
	let selectedItemIndex: number | null = null;
	
	function handleDragStart(e: DragEvent, index: number) {
		if (!sortable || !interactive) return;
		draggedItemIndex = index;
		isDragging = true;
		if (e.dataTransfer) {
			e.dataTransfer.effectAllowed = "move";
			e.dataTransfer.setData("text/plain", index.toString());
		}
	}

	function handleDragEnd(e: DragEvent) {
		isDragging = false;
	}

	function handleDrop(e: DragEvent, dropIndex: number) {
		if (!sortable || !interactive || draggedItemIndex === null) return;
		e.preventDefault();
		
		if (draggedItemIndex !== dropIndex) {
			moveItem(draggedItemIndex, dropIndex);
		}
		
		draggedItemIndex = null;
		isDragging = false;
	}

	function handleDragOver(e: DragEvent) {
		if (!sortable || !interactive) return;
		e.preventDefault();
		e.dataTransfer!.dropEffect = "move";
	}
	
	function selectItem(index: number) {
		if (!sortable || !interactive) return;
		selectedItemIndex = index;
		
		// Focus on the selected item
		setTimeout(() => {
			const buttons = document.querySelectorAll(".sortable-item");
			if (buttons && buttons[index]) {
				(buttons[index] as HTMLElement).focus();
			}
		}, 0);
	}
	
	function moveItem(fromIndex: number, toIndex: number) {
		if (!sortable || !interactive || fromIndex < 0 || fromIndex >= value.length || toIndex < 0 || toIndex >= value.length) 
			return;
		
		const newValue = [...value];
		const [itemToMove] = newValue.splice(fromIndex, 1);
		newValue.splice(toIndex, 0, itemToMove);
		value = newValue;
		selectedItemIndex = toIndex;
		
		gradio.dispatch("input");
		
		requestAnimationFrame(() => {
			const items = document.querySelectorAll(".sortable-item");
			if (items && items[toIndex]) {
				(items[toIndex] as HTMLElement).focus();
			}
		});
	}

	// Function to move two adjacent items
	function swapAdjacentItems(index1: number, index2: number) {
		if (!sortable || !interactive) return;
		if (index1 < 0 || index1 >= value.length || index2 < 0 || index2 >= value.length) return;
		if (Math.abs(index1 - index2) !== 1) return;
		
		const newValue = [...value];
		[newValue[index1], newValue[index2]] = [newValue[index2], newValue[index1]];
		value = newValue;
		selectedItemIndex = index2;
		
		gradio.dispatch("input");
		
		// Focus on the moved item
		requestAnimationFrame(() => {
			const items = document.querySelectorAll(".sortable-item");
			if (items && items[index2]) {
				(items[index2] as HTMLElement).focus();
			}
		});
	}

	// Function to move item up
	function simpleMoveUp(index: number) {
		if (index <= 0) return;
		swapAdjacentItems(index, index - 1);
	}

	// Function to move item down
	function simpleMoveDown(index: number) {
		if (index >= value.length - 1) return;
		swapAdjacentItems(index, index + 1);
	}

	// Optimized keyboard event handler for all keys
	function handleKeyDown(e: KeyboardEvent, index: number) {
		if (!sortable || !interactive) return;
		
		e.stopPropagation(); // Prevent event propagation to document
		
		switch (e.key) {
			case "Escape":
			case "Enter":
				e.preventDefault();
				selectedItemIndex = null;
				draggedItemIndex = null;
				show_order = false; // Disable order display
				// Focus on toggle button
				const toggleButton = document.querySelector(".toggle-button");
				if (toggleButton) {
					(toggleButton as HTMLElement).focus();
				}
				break;
				
			case " ":
				e.preventDefault();
				if (draggedItemIndex === null) {
					draggedItemIndex = index;
				} else {
					if (draggedItemIndex !== index) {
						moveItem(draggedItemIndex, index);
					}
					draggedItemIndex = null;
				}
				break;
				
			case "ArrowUp":
				if (index > 0) {
					e.preventDefault();
					simpleMoveUp(index);
					// Focus on new position
					requestAnimationFrame(() => {
						const items = document.querySelectorAll(".sortable-item");
						if (items && items[index - 1]) {
							(items[index - 1] as HTMLElement).focus();
						}
					});
				}
				break;
				
			case "ArrowDown":
				if (index < value.length - 1) {
					e.preventDefault();
					simpleMoveDown(index);
					// Focus on new position
					requestAnimationFrame(() => {
						const items = document.querySelectorAll(".sortable-item");
						if (items && items[index + 1]) {
							(items[index + 1] as HTMLElement).focus();
						}
					});
				}
				break;
		}
	}
	
	$: disabled = !interactive;

	$: if (JSON.stringify(old_value) !== JSON.stringify(value)) {
		old_value = [...value];
		gradio.dispatch("change");
	}
	
	function toggleOrderSection() {
		show_order = !show_order;
	}

	// Update translations when they change
	$: if (translations) {
		checkTranslations();
	}

	onMount(() => {
		checkTranslations();
		setTranslationsFromBackend();
		
		if (value.length > 0) {
			gradio.dispatch("input");
		}
	});
</script>

<Block
	{visible}
	{elem_id}
	{elem_classes}
	type="fieldset"
	{container}
	{scale}
	{min_width}
>
	<StatusTracker
		autoscroll={gradio.autoscroll}
		i18n={gradio.i18n}
		{...loading_status}
		queue_position={queue_position}
		queue_size={queue_size}
		status={status}
		on:clear_status={() => gradio.dispatch("clear_status")}
	/>
	
	<div class="header-container">
	<BlockTitle {root} {show_label} {info}>{label}</BlockTitle>
		
		{#if sortable && value.length > 0}
			<div class="order-toggle">
				<button type="button" class="toggle-button" on:click={toggleOrderSection}>
					<span class="toggle-icon">{show_order ? '▼' : '▶'}</span>
					<span class="toggle-text">{show_order ? getTranslation("hide_order") : getTranslation("show_order")}</span>
				</button>
			</div>
		{/if}
	</div>

	{#if sortable && value.length > 0 && show_order}
		<div class="sorted-items-section">
			<div class="sorted-items-heading">{getTranslation("priority_order")}</div>
			
			{#if selectedItemIndex !== null}
				<div class="active-item-indicator">
					<span class="indicator-icon">⌨️</span>
					<span class="indicator-text">{getTranslation("arrow_keys_guide")}</span>
				</div>
			{/if}
			
			<ul class="sorted-items" role="listbox" aria-label={getTranslation("sortable_items_list")}>
				{#each value as selectedValue, index}
					{#each choices as [display_value, internal_value]}
						{#if internal_value === selectedValue}
							<li class="sortable-item-container">
								<button 
									type="button"
									class="sortable-item" 
									draggable={interactive}
									on:dragstart={(e) => handleDragStart(e, index)}
									on:dragend={handleDragEnd}
									on:dragover={handleDragOver}
									on:drop={(e) => handleDrop(e, index)}
									on:click={() => selectItem(index)}
									on:keydown={(e) => handleKeyDown(e, index)}
									role="option"
									aria-selected={draggedItemIndex === index || selectedItemIndex === index}
									aria-label={`${display_value}. ${getTranslation("keyboard_usage_guide")}`}
									disabled={!interactive}
									class:dragging={draggedItemIndex === index && isDragging}
									class:selected={selectedItemIndex === index}
								>
									<span class="drag-handle" aria-hidden="true">&#8597;</span>
									<span class="item-value">{display_value}</span>
									{#if draggedItemIndex === index}
										<span class="sr-only">{getTranslation("moving")}</span>
									{/if}
									<div class="keyboard-controls" aria-hidden="true">
										{#if index > 0}
											<button 
												type="button" 
												class="keyboard-control-button" 
												on:click|stopPropagation={() => simpleMoveUp(index)}
												aria-label={getTranslation("move_up")}
												tabindex="-1"
												title={getTranslation("move_up")}
											>
												▲
											</button>
										{/if}
										{#if index < value.length - 1}
											<button 
												type="button" 
												class="keyboard-control-button" 
												on:click|stopPropagation={() => simpleMoveDown(index)}
												aria-label={getTranslation("move_down")}
												tabindex="-1"
												title={getTranslation("move_down")}
											>
												▼
											</button>
										{/if}
									</div>
								</button>
							</li>
						{/if}
					{/each}
				{/each}
			</ul>
			<div class="keyboard-instructions" aria-hidden="true">
				<p class="instructions-heading">{getTranslation("keyboard_instructions")}:</p>
				<ul class="instructions-list">
					<li class="instruction-item">{getTranslation("arrow_keys_guide")} <kbd>↑</kbd> <kbd>↓</kbd></li>
					<li class="instruction-item">{getTranslation("enter_space_guide")} <kbd>Space</kbd></li>
					<li class="instruction-item">{getTranslation("escape_guide")} <kbd>Esc</kbd> / <kbd>Enter</kbd></li>
				</ul>
			</div>
		</div>
	{/if}

	<div class="wrap" data-testid="checkbox-group">
		{#each choices as [display_value, internal_value], i}
			<label class:disabled class:selected={value.includes(internal_value)}>
				<input
					{disabled}
					on:change={() => toggle_choice(internal_value)}
					on:input={(evt) =>
						gradio.dispatch("select", {
							index: i,
							value: internal_value,
							selected: evt.currentTarget.checked
						})}
					on:keydown={(event) => {
						if (event.key === "Enter") {
							toggle_choice(internal_value);
							gradio.dispatch("select", {
								index: i,
								value: internal_value,
								selected: !value.includes(internal_value)
							});
						}
					}}
					checked={value.includes(internal_value)}
					type="checkbox"
					name={internal_value?.toString()}
					title={internal_value?.toString()}
				/>
				<span class="ml-2">{display_value}</span>
			</label>
		{/each}
	</div>
</Block>

<style>
	.header-container {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: var(--size-2);
		flex-wrap: wrap;
	}

	:global([dir="rtl"]) .header-container {
		flex-direction: row-reverse;
	}

	.wrap {
		display: flex;
		flex-wrap: wrap;
		gap: var(--checkbox-label-gap);
	}

	:global([dir="rtl"]) .wrap {
		direction: rtl;
	}

	:global([dir="rtl"]) .ml-2 {
		margin-right: var(--size-2);
		margin-left: 0;
	}

	:global([dir="rtl"]) .drag-handle {
		margin-left: var(--size-3);
		margin-right: 0;
	}

	:global([dir="rtl"]) .keyboard-controls {
		margin-right: var(--size-2);
		margin-left: 0;
	}

	:global([dir="rtl"]) .sortable-item.selected::before {
		right: -4px;
		left: auto;
		border-radius: 0 2px 2px 0;
	}

	:global([dir="rtl"]) .active-item-indicator {
		border-right: 3px solid var(--color-accent);
		border-left: none;
	}

	:global([dir="rtl"]) .instructions-list {
		padding-right: var(--size-4);
		padding-left: 0;
	}

	label {
		display: flex;
		align-items: center;
		transition: var(--button-transition);
		cursor: pointer;
		box-shadow: var(--checkbox-label-shadow);
		border: var(--checkbox-label-border-width) solid
			var(--checkbox-label-border-color);
		border-radius: var(--checkbox-border-radius);
		background: var(--checkbox-label-background-fill);
		padding: var(--checkbox-label-padding);
		color: var(--checkbox-label-text-color);
		font-weight: var(--checkbox-label-text-weight);
		font-size: var(--checkbox-label-text-size);
		line-height: var(--line-md);
	}

	label:hover {
		background: var(--checkbox-label-background-fill-hover);
	}
	label:focus {
		background: var(--checkbox-label-background-fill-focus);
	}
	label.selected {
		background: var(--checkbox-label-background-fill-selected);
		color: var(--checkbox-label-text-color-selected);
		border-color: var(--checkbox-label-border-color-selected);
	}

	label > * + * {
		margin-left: var(--size-2);
	}

	input {
		--ring-color: transparent;
		position: relative;
		box-shadow: var(--checkbox-shadow);
		border: var(--checkbox-border-width) solid var(--checkbox-border-color);
		border-radius: var(--checkbox-border-radius);
		background-color: var(--checkbox-background-color);
		line-height: var(--line-sm);
	}

	input:checked,
	input:checked:hover,
	input:checked:focus {
		border-color: var(--checkbox-border-color-selected);
		background-image: var(--checkbox-check);
		background-color: var(--checkbox-background-color-selected);
	}

	input:checked:focus {
		border-color: var(--checkbox-border-color-focus);
		background-image: var(--checkbox-check);
		background-color: var(--checkbox-background-color-selected);
	}

	input:hover {
		border-color: var(--checkbox-border-color-hover);
		background-color: var(--checkbox-background-color-hover);
	}

	input:not(:checked):focus {
		border-color: var(--checkbox-border-color-focus);
	}

	input[disabled],
	.disabled {
		cursor: not-allowed;
	}

	input:hover {
		cursor: pointer;
	}

	.order-toggle {
		margin-left: var(--size-2);
	}

	:global([dir="rtl"]) .order-toggle {
		margin-right: var(--size-2);
		margin-left: 0;
	}

	.toggle-button {
		display: flex;
		align-items: center;
		gap: var(--size-1);
		background-color: var(--background-fill-primary);
		border: 1px solid var(--border-color-primary);
		border-radius: var(--radius-sm);
		padding: var(--size-1-5) var(--size-3);
		font-size: var(--text-sm);
		font-weight: var(--weight-medium);
		color: var(--body-text-color);
		cursor: pointer;
		transition: all 0.2s ease;
		box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
	}

	.toggle-button:hover {
		background-color: var(--background-fill-secondary);
		border-color: var(--color-accent-soft);
	}
	
	.toggle-button:focus {
		outline: none;
		box-shadow: 0 0 0 2px var(--color-accent-soft);
	}
	
	.toggle-icon {
		font-size: 0.7em;
		color: var(--color-accent);
		transition: transform 0.2s ease;
	}
	
	.sorted-items-section {
		margin-top: var(--size-2);
		margin-bottom: var(--size-4);
		padding: var(--size-2);
		border-radius: var(--radius-lg);
		background-color: var(--background-fill-secondary);
		border: 1px solid var(--border-color-primary);
		box-shadow: var(--shadow-drop);
		animation: fadeIn 0.3s ease;
	}
	
	@keyframes fadeIn {
		from { opacity: 0; transform: translateY(-10px); }
		to { opacity: 1; transform: translateY(0); }
	}

	.sorted-items-heading {
		margin-top: 0;
		margin-bottom: var(--size-2);
		font-size: var(--text-md);
		color: var(--body-text-color);
		font-weight: var(--weight-semibold);
		border-bottom: 1px solid var(--border-color-primary);
		padding-bottom: var(--size-1);
	}

	.sorted-items {
		margin-top: var(--size-2);
		display: flex;
		flex-direction: column;
		gap: var(--size-2);
		list-style: none;
		padding: 0;
	}
	
	.sortable-item-container {
		margin: 0;
		padding: 0;
	}

	.sortable-item {
		display: flex;
		align-items: center;
		width: 100%;
		text-align: left;
		padding: var(--size-2) var(--size-3);
		border: 1px solid var(--border-color-primary);
		border-radius: var(--radius-md);
		background-color: var(--background-fill-primary);
		cursor: grab;
		transition: all 0.2s ease;
		box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
	}

	:global([dir="rtl"]) .sortable-item {
		text-align: right;
	}

	.sortable-item:hover {
		background-color: var(--background-fill-secondary);
		transform: translateY(-1px);
		box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
	}
	
	.sortable-item:focus {
		outline: none;
		box-shadow: 0 0 0 2px var(--color-accent);
	}
	
	.sortable-item[disabled] {
		opacity: 0.6;
		cursor: not-allowed;
	}

	.sortable-item[aria-selected="true"],
	.sortable-item.selected {
		background-color: var(--background-fill-secondary);
		box-shadow: 0 0 0 2px var(--color-accent);
		border-color: var(--color-accent);
		position: relative;
	}
	
	.sortable-item.selected::before {
		content: "";
		position: absolute;
		left: -4px;
		top: 50%;
		transform: translateY(-50%);
		width: 4px;
		height: 70%;
		background-color: var(--color-accent);
		border-radius: 2px 0 0 2px;
	}
	
	.sortable-item.dragging {
		opacity: 0.8;
		transform: scale(1.02);
		box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
		z-index: 1000;
		background-color: var(--background-fill-secondary);
	}

	.drag-handle {
		margin-right: var(--size-3);
		color: var(--body-text-color-subdued);
		cursor: grab;
		user-select: none;
		font-size: 1.2em;
	}

	.item-value {
		flex: 1;
		font-weight: var(--weight-medium);
	}
	
	.keyboard-controls {
		display: flex;
		flex-direction: column;
		gap: 4px;
		margin-left: var(--size-2);
	}
	
	.keyboard-control-button {
		background: transparent;
		border: none;
		color: var(--body-text-color-subdued);
		cursor: pointer;
		font-size: 14px;
		padding: 2px;
		line-height: 1;
		transition: all 0.2s ease;
		border-radius: 50%;
		width: 20px;
		height: 20px;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	
	.keyboard-control-button:hover {
		color: var(--color-accent);
		background-color: var(--background-fill-primary);
	}
	
	.keyboard-control-button:focus {
		outline: none;
		color: var(--color-accent);
	}
	
	.keyboard-instructions {
		margin-top: var(--size-3);
		font-size: var(--text-xs);
		color: var(--body-text-color-subdued);
		background-color: var(--background-fill-primary);
		border-radius: var(--radius-md);
		padding: var(--size-2);
		border: 1px dashed var(--border-color-primary);
	}
	
	.keyboard-instructions p {
		margin: 0 0 var(--size-1) 0;
		font-weight: var(--weight-medium);
	}
	
	.keyboard-instructions ul {
		margin: 0;
		padding-left: var(--size-4);
	}
	
	.keyboard-instructions li {
		margin-bottom: var(--size-1);
	}
	
	kbd {
		background-color: var(--background-fill-secondary);
		border: 1px solid var(--border-color-primary);
		border-radius: 3px;
		box-shadow: 0 1px 0 var(--border-color-primary);
		display: inline-block;
		font-size: 0.7em;
		font-weight: bold;
		line-height: 1;
		padding: 2px 4px;
		white-space: nowrap;
		color: var(--color-accent);
	}
	
	.sr-only {
		position: absolute;
		width: 1px;
		height: 1px;
		padding: 0;
		margin: -1px;
		overflow: hidden;
		clip: rect(0, 0, 0, 0);
		white-space: nowrap;
		border-width: 0;
	}
	
	.active-item-indicator {
		display: flex;
		align-items: center;
		gap: var(--size-2);
		margin-bottom: var(--size-2);
		padding: var(--size-1) var(--size-2);
		background-color: var(--background-fill-primary);
		border-radius: var(--radius-sm);
		font-size: var(--text-xs);
		color: var(--body-text-color);
		border-left: 3px solid var(--color-accent);
	}
	
	.indicator-icon {
		font-size: 1.2em;
	}
	
	.toggle-text {
		font-weight: var(--weight-medium);
	}
	
	.indicator-text {
		font-weight: var(--weight-medium);
	}
	
	.instructions-heading {
		margin: 0 0 var(--size-1) 0;
		font-weight: var(--weight-medium);
	}
	
	.instructions-list {
		margin: 0;
		padding-left: var(--size-4);
	}
	
	.instruction-item {
		margin-bottom: var(--size-1);
	}
</style>
