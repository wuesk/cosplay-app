<script lang="ts">
    import { page } from "$app/state";
	import Costumes from "$lib/components/profile/Costumes.svelte";

    $: username = page.params.username;
</script>


<div class="profile-page">
    <!-- 
        TODO: Photographer has a pfp of themselves
        A cosplayer has a pfp which is their favourite photo, can select multiple
     -->
    <div class="profile">
        <div class="main-image">
            <img/>
        </div>
        <div class="image-gallery">
            <!-- TODO: actual gallery, section hidden for photographer? Unless they want to showcase their favourite photos -->
            <div class="image-gallery-scroll">
                &lt;
            </div>
            <div class="image-selection"></div>
            <div class="image-selection"></div>
            <div class="image-selection"></div>
            <div class="image-selection"></div>
            <div class="image-gallery-scroll">
                &gt;
            </div>
        </div>
        <div class="username">
        <!--TODO: Photographer / cosplayer (maybe both?) + verified status -->
            <h1>👘📷 {username}</h1>
        </div>
        <!-- TODO: For cosplayer: a list of costumes. -->
        <Costumes/>
        <div class="description">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sodales ante massa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent semper, eros ut consequat cursus, tellus diam elementum risus, eget blandit augue risus ut nulla. In ac nunc ultricies, pulvinar lacus eu, pretium nunc. Vestibulum rhoncus sit amet nunc cursus iaculis. Nam congue tellus id congue placerat. Curabitur nisi ex, facilisis a nisi malesuada, tristique tincidunt sem. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam ut ante lacus. Proin finibus placerat eros rutrum pulvinar.
        </div>
    </div>

</div>

<style>
    .profile-page {
        text-align: center;
    }

    .main-image {
        width: 400px;
        height: 400px;
        margin: 0 auto;
        border: 2px solid grey;
        border-radius: 20px;
    }

    .image-gallery {
        width: 600px;
        margin: 10px auto;
    }

    .image-gallery-scroll {
        display: inline-block;
        font-size: 80px;
    }

    .image-selection {
        display: inline-block;
        width: 100px;
        height: 100px;
        border: 2px solid grey;
        border-radius: 10px;
    }
</style>
