import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  plugins: [svelte()],
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: {
      input: {
        index: 'Index.svelte',
        example: 'Example.svelte'
      },
      output: {
        entryFileNames: '[name].js'
      }
    }
  }
}); 