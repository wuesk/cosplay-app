<script lang="ts">
	import { goto } from "$app/navigation";
	import type { IMenu } from "$lib/types/core";
    import { onMount } from "svelte";

    export let name: string = "";
    export let color: string = "royalblue";
    export let menus: IMenu[] = [];

    //TODO: Move to a shared const
    let brandMenus: IMenu[] = [
        { name: "profiles", url: '/profiles', color: "royalblue" },
        { name: "database", url: '/database', color: "purple" },
        { name: "map", url: '/map', color: "green" },
        { name: "events🔒", url: "/events", color: "olive" }
    ]; // New prop for brand dropdown items
    
    let showDropdown = false;
    let dropdownRef: HTMLDivElement;

    async function handleNav(route: string) {
        try {
            showDropdown = false; // Close dropdown after navigation
            await goto(route);
        } catch (error) {
            console.error('Navigation failed! ', error);
        }
        console.log(`Navigating to ${route}`);
    }

    function toggleDropdown() {
        showDropdown = !showDropdown;
    }

    // Close dropdown when clicking outside
    onMount(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (dropdownRef && !dropdownRef.contains(event.target as Node)) {
                showDropdown = false;
            }
        };

        document.addEventListener('click', handleClickOutside);

        return () => {
            document.removeEventListener('click', handleClickOutside);
        };
    });
</script>

<div class="navbar" style="background-color: {color}">
    <ul>
        <li class="brand" bind:this={dropdownRef}>
            <button on:click={toggleDropdown}>cosplan.me {name}</button>
            {#if showDropdown}
                <div class="dropdown">
                    {#each brandMenus as item, index}
                        <button 
                            on:click={() => handleNav(item.url)} 
                            style="background-color: {item.color || 'royalblue'};"
                        >
                            cosplan.me {item.name}
                        </button>
                    {/each}
                </div>
            {/if}
        </li>
        {#each menus as menu}
            <li>
                <button on:click={() => handleNav(menu.url)}>{menu.name}</button>
            </li>
        {/each}
    </ul>
</div>

<style>
    .navbar {
        width: 100vw;
        height: 40px;
        background-color: royalblue;
    }

    ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
        height: 100%;
        display: flex;
        align-items: center;
    }
    
    li {
        font-size: 16px;
        color: white;
        cursor: pointer;
        transition: background-color 0.2s;
        padding: 0;
    }

    li button {
        background: none;
        border: none;
        color: white;
        padding: 11px 16px;
        font-size: 16px;
        cursor: pointer;
        width: 100%;
        height: 100%;
        transition: background-color 0.2s;
    }

    li button:hover {
        background-color: rgba(255, 255, 255, 0.1);
    }

    .brand {
        font-weight: bold;
        background-color: rgba(0, 0, 0, 0.1);
        position: relative; /* Needed for dropdown positioning */
        min-width: 200px;
    }

    .brand:hover {
        background-color: rgba(0, 0, 0, 0.2);
    }

    .dropdown {
        position: absolute;
        top: 100%;
        left: 0;
        display: flex;
        flex-direction: column;
        min-width: 100%;
        background-color: royalblue;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        z-index: 100;
    }

    .dropdown button {
        text-align: left;
        padding: 12px 16px;
        min-width: 200px;
        font-weight: normal;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }

    .dropdown button:hover {
        background-color: rgba(255, 255, 255, 0.2);
    }
</style>