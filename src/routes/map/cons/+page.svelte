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

<div class="container">
    <h1>Anime cons</h1>
    <div class="filters">
        <input type="text" placeholder="Search" bind:value={filterName}>

        <select bind:value={filterCountry}>
            <option value=''>All Countries</option>
            {#each countries as country}
                <option value={country}>{country}</option>
            {/each}
        </select>

        <select bind:value={filterCity}>
            <option value=''>All Cities</option>
            {#each cities as city}
                <option value={city}>{city}</option>
            {/each}
        </select>

        <input type="number" min=0 max=10 bind:value={filterRating}>
    </div>
    <table class="cons-table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Location</th>
                <th>Date</th>
                <th>Rating</th>
            </tr>
        </thead>
        <tbody>
            {#each filteredCons as con}
                <tr>
                    <td>{con.name}</td>
                    <td>{`${con.city} (${con.country})`}</td>
                    <td>{formatDate(con.startDate)} - {formatDate(con.endDate)}</td>
                    <td>{con.rating} / 10</td>
                </tr>
            {/each}
        </tbody>
    </table>
</div>

<style>
    .container {
        background-color: rgb(97, 163, 85);
        width: 100%;
    }

    .container h1 {
        margin-top: 0px;
        margin-bottom: 0px;
    }

    .cons-table th,
    .cons-table td {
        padding: 6px 10px;
    }

    .cons-table tbody tr:nth-child(even),
    .cons-table thead tr {
        background-color: rgba(0,0,0,0.08);
    }

    .filters input, .filters select {
        padding: 6px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }
</style>