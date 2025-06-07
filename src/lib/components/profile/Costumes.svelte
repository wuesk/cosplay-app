<script lang="ts">
	import Pill from "$lib/components/core/Pill.svelte";

	let costumes = [
		{
			name: 'Hu Tao',
			color: '#FF0000'
		},
		{
			name: 'Xayah (Battle Bat ver.)',
			color: '#0000FF'
		},
		{
			name: 'Dan Heng',
			color: '#00FF00'
		},
		{
			name: 'Raiden Shogun',
			color: '#FF00FF'
		},
		{
			name: 'Dan Heng (Imbibitor Lunae ver.)',
			color: '#FFFF00'
		},
		{
			name: 'Jane Doe',
			color: '#00FFFF'
		},
		{
			name: 'Saber Alter',
			color: '#000000'
		}
	];
</script>

<div class="costumes">
    {#each costumes as costume}
        <Pill color="{costume.color}">
            <a href="/character/1">
                {costume.name}
            </a>
        </Pill>
    {/each}
</div>

<style>
    .costumes {
        width: 500px;
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        padding: 16px;
        margin: 0 auto;
    }

    a {
        color: white;
    }
</style>