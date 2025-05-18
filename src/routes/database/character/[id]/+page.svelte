<script lang="ts">
    import { page } from "$app/state";
	import Profile from "$lib/components/core/Profile.svelte";

    $: username = page.params.username;
</script>

<div class="character-page">
   <Profile /> 
</div>