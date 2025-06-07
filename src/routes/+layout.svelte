<script lang="ts">
	import Navbar from '$lib/components/ui/navbar/Navbar.svelte';
	import '../app.css';
</script>

<div class="fixed inset-0 flex overflow-hidden">
	<Navbar className="w-[70px] h-full shrink-0 shadow-md shadow-r"/>
	<div class="flex-1 overflow-auto">
		<slot />
	</div>
</div>

<style>
	/* Custom shadow utility to create right-side shadow only */
	:global(.shadow-r) {
		box-shadow: 4px 0 6px -1px rgba(0, 0, 0, 0.1), 2px 0 4px -2px rgba(0, 0, 0, 0.1);
	}
</style>