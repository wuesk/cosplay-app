<script lang="ts">
    let popCharacters = [
        { id: "xayah", name: "Xayah (League of Legends" },
        { id: "ahri", name: "Ahri (League of Legends" },
        { id: "janedoe", name: "Jane Doe (Zenless Zone Zero)" },
        { id: "ghostmw", name: "Ghost (Call of Duty MW)" },
        { id: "hutao", name: "Hu Tao (Genshin Impact) "}
    ]

    let popSeries = [
        { id: "leagueoflegends", name: "League of Legends" },
        { id: "genshin", name: "Genshin Impact" },
        { id: "starrail", name: "Honkai: Star Rail" }, 
        { id: "zzz", name: "Zenless Zone Zero" },
        { id: "wuwa", name: "Wuthering Waves" }
    ]
</script>

<div class="database-landing">
    <h1>Welcome to cosplan.me's database!</h1>
    <p>Here you can find and learn about characters and series they belong to!</p>

    <div class="news">
        <!-- TODO: I love and miss marquees, let's use them kek -->
        <!-- svelte-ignore a11y_distracting_elements -->
        <marquee behavior="scroll" direction="right">hurrr distracting elements</marquee>
    </div>
    <div class="pop-wrapper">
        <!-- TODO: Bruh, you could implement actual sorting by popularit -->
        <div class="pop characters">
            <h2>Popular characters</h2>
            <ul>
                <!-- TODO: Name + (series) -->
                {#each popCharacters as popCharacter}
                    <li><a href="/database/character/{popCharacter.id}">{popCharacter.name}</a></li>
                {/each}
            </ul>
        </div>
        <div class="pop series">
            <h2>Popular series</h2>
            <ul>
                {#each popSeries as popSerie}
                    <li><a href="/database/series/{popSerie.id}">{popSerie.name}</a></li>
                {/each}
            </ul>
        </div>
    </div>
</div>

<style>
    .pop-wrapper {
    }

    .pop {
        display: inline-block;
    }
</style>