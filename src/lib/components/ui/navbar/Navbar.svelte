<script lang="ts">
	import { goto } from "$app/navigation";
	import NavbarButton from "./NavbarButton.svelte";

    export let className: string = '';
    let navItems: any[] = [
        {
            label: "Profiles",
            icon: "🗿",
            onClick: () => goto("/profiles"),
        },
        {
            label: "Events",
            icon: "🎉",
            onClick: () => goto("/events"),
        },
        {
            label: "Map",
            icon: "🗺️",
            onClick: () => goto("/map"),
        },
        {
            label: "Database",
            icon: "💾",
            onClick: () => goto("/database"),
        },
        {
            label: "Settings",
            icon: "⚙️",
            onClick: () => console.log("Settings!"),
        }
    ];
</script>

<nav class={`flex flex-col items-center py-4 bg-stone-700 ${className}`}>
    <div class="w-full relative mb-10">
        <div class="absolute top-38 left-3 origin-top-left -rotate-90 text-3xl text-stone-800 px-3 py-1 rounded font-semibold">
            COSPLAN
        </div>
    </div>
    <div class="flex flex-col gap-3 my-auto">
        {#each navItems as item}
            <NavbarButton item={item} />
        {/each}
    </div>
</nav>

<div class="fixed bottom-3 left-15 -rotate-90 origin-bottom-left text-stone-800 font-semibold text-xs">
    <div class="text-center">
        Created with love<br>
        For my dear friends<br>
        By jesx 2025
    </div>
</div>

<style>
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
</style>