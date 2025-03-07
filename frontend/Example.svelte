<script lang="ts">
	import { onMount } from "svelte";
	
	export let value: string[];
	export let type: "gallery" | "table";
	export let selected = false;
	export let choices: [string, string | number][];
	export let sortable = true;

	let names: string[] = [];
	let names_string = "";
	
	// به‌روزرسانی نمایش نام‌ها هر زمان که مقدار یا انتخاب‌ها تغییر می‌کند
	$: {
		names = value
			.map(
				(val) =>
					(
						choices.find((pair) => pair[1] === val) as
							| [string, string | number]
							| undefined
					)?.[0]
			)
			.filter((name): name is string => name !== undefined);
		names_string = names.join(", ");
	}
	
	// اطمینان از اعمال مقدار اولیه
	onMount(() => {
		// به‌روزرسانی فوری
		names = value
			.map(
				(val) =>
					(
						choices.find((pair) => pair[1] === val) as
							| [string, string | number]
							| undefined
					)?.[0]
			)
			.filter((name): name is string => name !== undefined);
		names_string = names.join(", ");
	});
</script>

<div
	class:table={type === "table"}
	class:gallery={type === "gallery"}
	class:selected
	class:sortable
>
	{#if sortable && names.length > 1}
		<div class="ordered-list">
			<ol>
				{#each names as name}
					<li>{name}</li>
				{/each}
			</ol>
		</div>
	{:else}
		{names_string}
	{/if}
</div>

<style>
	.gallery {
		padding: var(--size-1) var(--size-2);
	}
	
	.ordered-list ol {
		margin: 0;
		padding-left: var(--size-4);
	}
	
	.ordered-list li {
		margin-bottom: var(--size-1);
	}
</style>
