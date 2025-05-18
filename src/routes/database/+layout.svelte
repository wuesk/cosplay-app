<script lang="ts">
	import Navbar from "$lib/components/core/Navbar.svelte";
	import type { IMenu } from "$lib/types/core";

	let menus: IMenu[] = [
		{ name: "characters", url: "char" },
		{ name: "series", url: "series" },
		{ name: "favourites", url: "favourites" },
	]
</script>

<div class="database">
	<Navbar menus={menus} name={"database"} color={"purple"}/>
	<div class="content">
  		<slot />
	</div>
</div>

<style>
	.database {
		width: 100%;
	}
</style>
