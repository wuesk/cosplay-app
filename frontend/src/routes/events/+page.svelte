<script lang="ts">
    const cons: any[] = [
        {
            name: "Festiwal Fantastyki Pyrkon",
            country: "Poland",
            city: "Poznań",
            startDate: new Date('2025-06-13'),
            endDate: new Date('2025-06-15'),
            rating: 0.5,
        },
        {
            name: "Aicon",
            country: "Poland",
            city: "Rybnik",
            startDate: new Date('2025-03-22'),
            endDate: new Date('2025-03-23'),
            rating: 5.3,
        },
        {
            name: "Festiwal Hanami",
            country: "Poland",
            city: "Ursynów",
            startDate: new Date('2025-04-12'),
            endDate: new Date('2025-04-13'),
            rating: 6.9,
        },
        {
            name: "Maginifcon EXPO",
            country: "Poland",
            city: "Kraków",
            startDate: new Date('2025-05-23'),
            endDate: new Date('2025-05-25'),
            rating: 10.0,
        },
        {
            name: "Dokomi",
            country: "Germany",
            city: "Düsseldorf",
            startDate: new Date('2025-06-06'),
            endDate: new Date('2025-06-08'),
            rating: 10.0,
        },
    ]

    let filterName = '';
    let filterCountry = '';
    let filterCity = '';
    let filterRating = 0;

    $: filteredCons = cons.filter((con) => {
        const matchesName = con.name.toLowerCase().includes(filterName.toLocaleLowerCase());
        const matchesCountry = filterCountry ? con.country === filterCountry : true;
        const matchesCity = filterCity ? con.city === filterCity : true;
        const minimumRating = con.rating > filterRating;
        return matchesName && matchesCountry && matchesCity && minimumRating;
    });

    $: countries = [...new Set(cons.map(con => con.country))];
    $: cities = filterCountry
        ? [...new Set(cons.filter(c => c.country === filterCountry).map(c => c.city))]
        : [...new Set(cons.map(c => c.city))];

    function formatDate(dateString: string): string {
        const date = new Date(dateString);
        const day = String(date.getDate()).padStart(2, '0');
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const year = date.getFullYear();
        return `${day}-${month}-${year}`;
    }        
</script>

<div class="w-full min-h-screen bg-green-800 text-white p-6">
    <h1 class="text-3xl font-bold mb-6">Anime cons</h1>
    
    <div class="flex flex-wrap gap-4 mb-6">
        <input 
            type="text" 
            placeholder="Search" 
            bind:value={filterName}
            class="px-4 py-2 bg-green-700 border border-green-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-400 text-white placeholder-green-300"
        >

        <select 
            bind:value={filterCountry}
            class="px-4 py-2 bg-green-700 border border-green-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-400 text-white"
        >
            <option value=''>All Countries</option>
            {#each countries as country}
                <option value={country}>{country}</option>
            {/each}
        </select>

        <select 
            bind:value={filterCity}
            class="px-4 py-2 bg-green-700 border border-green-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-400 text-white"
        >
            <option value=''>All Cities</option>
            {#each cities as city}
                <option value={city}>{city}</option>
            {/each}
        </select>

        <div class="flex items-center gap-2">
            <span class="text-sm">Min Rating:</span>
            <input 
                type="number" 
                min=0 
                max=10 
                bind:value={filterRating}
                class="px-4 py-2 w-20 bg-green-700 border border-green-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-400 text-white"
            >
        </div>
    </div>
    
    <div class="max-w-[1000px] overflow-x-auto rounded-lg shadow-lg">
        <table class="w-full border-collapse">
            <thead>
                <tr class="bg-green-900 text-left">
                    <th class="px-6 py-3 font-semibold">Name</th>
                    <th class="px-6 py-3 font-semibold">Location</th>
                    <th class="px-6 py-3 font-semibold">Date</th>
                    <th class="px-6 py-3 font-semibold">Rating</th>
                </tr>
            </thead>
            <tbody>
                {#each filteredCons as con, i}
                    <tr class={i % 2 === 0 ? 'bg-green-700' : 'bg-green-750' + "hover:bg-green-650 transition-colors"}>
                        <td class="px-6 py-4 border-t border-green-600">{con.name}</td>
                        <td class="px-6 py-4 border-t border-green-600">{`${con.city} (${con.country})`}</td>
                        <td class="px-6 py-4 border-t border-green-600">{formatDate(con.startDate)} - {formatDate(con.endDate)}</td>
                        <td class="px-6 py-4 border-t border-green-600">
                            <div class="flex items-center">
                                <span class="mr-2">{con.rating.toFixed(1)}</span>
                                <div class="w-24 bg-green-900 rounded-full h-2">
                                    <div class="bg-yellow-400 h-2 rounded-full" style="width: {con.rating * 10}%"></div>
                                </div>
                            </div>
                        </td>
                    </tr>
                {/each}
            </tbody>
        </table>
    </div>

    {#if filteredCons.length === 0}
        <div class="mt-8 text-center p-6 bg-green-700 rounded-lg">
            <p class="text-lg">No conventions found matching your filters.</p>
        </div>
    {/if}
</div>

<style>
    /* Custom color classes for Tailwind */
    .bg-green-750 {
        background-color: rgba(16, 90, 60, 0.9);
    }
    
    .bg-green-650 {
        background-color: rgba(16, 120, 60, 1);
    }
</style>