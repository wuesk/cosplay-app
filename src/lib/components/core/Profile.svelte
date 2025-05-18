<script lang="ts">
	import Pill from "./Pill.svelte";

    let name = "Xayah";
    let title = "The Rebel"
    let description = "Xayah is a vastayan rebel and freedom fighter who uses deadly precision with her razor-sharp feather quills. Together with her soulmate Rakan, she fights to protect the ancestral lands of her people from human encroachment. Lethal and graceful, she can recall her feathers to deal devastating damage while using her ultimate ability to become briefly untargetable, making her a dangerous AD Carry champion.";
    let versions = [
        "Classic",
        "Cosmic Dusk",
        "Sweetheart",
        "SSG",
        "Star Guardian",
        "Elderwood",
        "Brave Phoenix",
        "Arcana",
        "Prestige Brave Phoenix",
        "Redeemed Star Guardian"
    ]

    let profileAttrs = [
        { key: "Series", value: "League of Legends"},
    ]

    let cosplays = [
        { creator: "Rolecos", img: "https://d2rbvftet3l7m9.cloudfront.net/media/catalog/product/cache/fbcee2066c1a88cee7adb7791f80419c/l/e/league_of_legends_xayah_game_cosplay_costumes0.jpg" },
        { creator: "Rolecos", img: "https://d2rbvftet3l7m9.cloudfront.net/media/catalog/product/cache/fbcee2066c1a88cee7adb7791f80419c/l/e/league_of_legends_xayah_game_cosplay_costumes0.jpg" }
    ]

    let image = "https://static.wikia.nocookie.net/lolesports_gamepedia_en/images/d/d3/Skin_Loading_Screen_Classic_Xayah.jpg";

    let versionDesc = "Once a Star Guardian who fought alongside Rakan, Xayah fell to darkness when confronted by Zoe's overwhelming power. Corrupted and transformed into a Dark Star Guardian, she now serves as one of Zoe's most powerful agents. Her once-bright feathers have turned dark and sinister, reflecting her fall from grace."
</script>

<div class="profile">
    <div class="stats">
        <h2>{name}</h2>
        <h4>{title}</h4>
        <div class="image-container">
            <img src="{image}" alt="{name}"/>
        </div>
        <table class="info-table">
            <tbody>
                <tr>
                    {#each profileAttrs as attr}
                        <td>{attr.key}</td>
                        <td>{attr.value}</td>
                    {/each}
                </tr>
            </tbody>
        </table>
    </div>
    <div class="info">
        <section class="description">
            <h2>Description</h2>
            <span>
                {description}
            </span>
        </section>
        <section class="version">
            <span>
                {#each versions as version}
                    <Pill color="#000099">{version}</Pill>
                {/each}
            </span>
        </section>
        <section class="version-description">
            <h4>Version description</h4>
            <span>
                {versionDesc}
            </span>
        </section>
        <section class="cosplay">
            <h4>Cosplay</h4>
            {#if cosplays.length == 0}
                <p>There're no known mass produced cosplays. Custom ones may exist.</p>
            {:else if cosplays.length == 1}
                <p>There's a cosplay made by {cosplays[0].creator}. Custom ones may also exist.</p>
                <img src="{cosplays[0].img}"/>
            {:else if cosplays.length > 1}
                <p>There're multiple cosplays produced. Custom ones may also exist.</p>
                {#each cosplays as cosplay}
                    <div class="cosplay-card">
                        <img src={cosplay.img} alt={cosplay.creator}/>
                        <h6>{cosplay.creator}</h6>
                    </div>
                {/each}
            {/if}
        </section>
    </div>
</div>

<style>
    .profile {
        border: 2px solid black;
        background-color: white;
        margin: 30px;
        min-height: 500px;
        display: flex;
        gap: 20px;
        padding: 20px;
    }

    .stats {
        width: 30%;
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    section:not(:last-child) {
        margin-bottom: 20px;
    }

    section.cosplay img {
        max-height: 200px;
    }

    .image-container {
        min-height: 300px;
    }

    .cosplay-card {
        display: inline-block;
    }

    .info {
        width: 70%;
    }

    h2, h4 {
        margin: 0;
    }
</style>