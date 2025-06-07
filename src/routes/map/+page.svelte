<script lang="ts">
	import { onMount } from 'svelte';
	import maplibre from 'maplibre-gl';
	import 'maplibre-gl/dist/maplibre-gl.css';
	import FlagIcon from '$lib/components/map/FlagIcon.svelte';
	import type { ILocation } from '$lib/types/map';
	import PlaceInfoCard from '$lib/components/map/PlaceInfoCard.svelte';

	let mapContainer: HTMLElement;
	let map: maplibre.Map;
	let selectedPlace: ILocation | null = null;

	const markers: maplibre.Marker[] = [];

	let places: ILocation[] = [
		{
			name: 'Dyniowe Love 🎃',
			lat: 54.2748056,
			lng: 18.6183611,
			description: 'Popular pumpkin-themed restaurant in Gdansk.',
            friendly: true,
            friendlyDescription: "It's popular place for photo sessions, they don't mind cosplayers",
            legal: true,
            paid: true,
			paidDescription: "20 PLN entry fee",
			parking: true,
			parkingDescription: "Free parking. May be completly full at later hours.",
			image: "https://ocdn.eu/pulscms-transforms/1/TlCk9kpTURBXy84ZmUwZTU0NDA0MmY2MWQ4NWY1ZDE5MzVhMzkwNTU5MC5qcGeSlQLNAjwAwsOVAgDNAtDCw94AA6EwAaExAaEzww"
		},
		{ 
            name: 'Plaża Babie Doły',
            lat: 54.5858125,
            lng: 18.5391169,
            description: 'Wild beach',
            friendly: true,
            friendlyDescription: "It's an rarely attended beach. Not much people here, even in the summer."
        },
		{ 
            name: 'Stanowisko Ogniowe',
            lat: 54.4958818,
            lng: 18.5613753,
            description: '',
            friendly: true
        },
		{
			name: 'Park Oliwski',
			lat: 54.4112192,
			lng: 18.5619759,
			description: "Park Oliwski offers stunning photography opportunities with its picturesque gardens, historic cathedral backdrop, charming bridges, and vibrant flower displays. Perfect for portraits, wedding photos and nature photography throughout all four seasons.",
			friendly: true,
			friendlyDescription: "Common place for photo sessions. Has a lot of visitors, especially in the summer, but they don't make problems either.",
			parking: true,
			parkingDescription: "Lot's of public parking spaces around the park, you can even find some free spots during weekends.",
			paid: false,
			paidDescription: "Free",
			link: "https://www.parkoliwski.gdansk.pl/chapter_76486.asp",
			image: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Parque_Adam_Mickiewicz%2C_Oliwa%2C_Gdansk%2C_Polonia%2C_2013-05-21%2C_DD_04.jpg/1280px-Parque_Adam_Mickiewicz%2C_Oliwa%2C_Gdansk%2C_Polonia%2C_2013-05-21%2C_DD_04.jpg"
		}
	];

	function markPlaces() {
		// Clear any existing markers
		markers.forEach((marker) => marker.remove());
		markers.length = 0;

		places.forEach((place) => {
			console.log('Adding marker at:', place.lng, place.lat);

			const marker = new maplibre.Marker({
				color: '#FF0000',
				scale: 1.2
			})
				.setLngLat([place.lng, place.lat])
				.addTo(map);

			// Add a popup with place name
			const popup = new maplibre.Popup({ offset: 25, closeButton: false })
				.setHTML(`<h3>${place.name}</h3>`)
				.setMaxWidth('300px');

			marker.setPopup(popup);

			// Add click event to select a place
			marker.getElement().addEventListener('click', () => {
				selectedPlace = place;
			});

			markers.push(marker);
		});

		// Initialize with the first place selected
		if (places.length > 0 && !selectedPlace) {
			selectedPlace = places[0];
		}
	}

	onMount(() => {
		map = new maplibre.Map({
			container: mapContainer,
			style: 'https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json', // Dark style to match theme
			center: [18.8, 54.15], // Initial center [lng, lat]
			zoom: 9
		});

		map.on('load', () => {
			console.log('Map loaded');
			markPlaces();
		});

		// Safety check - try adding markers after a short delay
		setTimeout(() => {
			if (markers.length === 0) {
				console.log('Retrying marker placement');
				markPlaces();
			}
		}, 1000);
	});

	function flyToPlace(place: ILocation | null) {
		if (!place) throw("Error, incorect place");

		selectedPlace = place;

		map.flyTo({
			center: [place.lng, place.lat],
			zoom: 15,
			essential: true
		});

		// Find and open the popup for this place
		markers.forEach((marker, index) => {
			if (places[index] === place) {
				marker.togglePopup();
			}
		});
	}
</script>

<div class="flex h-full w-full overflow-hidden bg-blue-950">
	<div class="w-1/4 min-w-[300px] h-full overflow-y-auto shadow-md p-4 bg-blue-950 text-blue-50">
		<h2 class="text-2xl font-bold mb-4 text-blue-100">Locations</h2>
		
		<div class="mb-5">
			<select 
				on:change={(e) => flyToPlace(places[e.target.value])}
				class="w-full p-3 text-base rounded-lg border border-blue-700 bg-blue-800 text-blue-50 cursor-pointer shadow-sm transition-all duration-300 ease-in-out appearance-none focus:outline-none focus:ring-2 focus:ring-blue-400 hover:border-blue-500"
			>
				<option value="" disabled selected class="bg-blue-800">Select a place</option>
				{#each places as place, i}
					<option value={i} selected={selectedPlace === place} class="bg-blue-800 p-2">
						{place.name}
					</option>
				{/each}
			</select>
		</div>

		{#if selectedPlace}
			<div>
				<h2 class="text-2xl font-bold mb-4 text-blue-100">Selected Location</h2>
				<PlaceInfoCard 
					place={selectedPlace} 
					onCenterMap={() => flyToPlace(selectedPlace)} 
				/>
			</div>
		{/if}
	</div>
	
	<div id="map" bind:this={mapContainer} class="flex-1 h-full relative"></div>
</div>

<style>
	/* Override global map styles to match the theme */
	:global(.maplibregl-marker) {
		cursor: pointer;
		z-index: 10;
	}

	:global(.maplibregl-popup-content) {
		padding: 10px;
		border-radius: 5px;
		background-color: #1e3a8a;
		color: #eff6ff;
		border: 1px solid #3b82f6;
	}
	
	:global(.maplibregl-popup-tip) {
		border-top-color: #3b82f6 !important;
		border-bottom-color: #3b82f6 !important;
	}
	
	:global(.maplibregl-popup h3) {
		color: #eff6ff;
		font-weight: bold;
		margin: 0;
	}
	
	:global(.maplibregl-ctrl-group) {
		background-color: #1e3a8a !important;
		border: 1px solid #3b82f6 !important;
	}
	
	:global(.maplibregl-ctrl button) {
		color: #eff6ff !important;
	}
</style>