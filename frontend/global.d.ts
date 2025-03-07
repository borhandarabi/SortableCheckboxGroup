/// <reference types="svelte" />

declare module '*.svelte' {
  export { SvelteComponentDev as default } from 'svelte/internal';
}

// برای رویدادهای drag & drop
interface DragEvent extends Event {
  dataTransfer: DataTransfer;
} 