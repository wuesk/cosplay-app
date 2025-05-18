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
			name: 'Zamek w Malborku',
			lat: 54.039816,
			lng: 19.028027,
			description: 'The Castle of the Teutonic Order in Malbork, a UNESCO World Heritage Site',
            friendly: true,
			image: "https://www.podrozepoeuropie.pl/system/gallery/images/images/000/005/020/large/Zamek-w-Malborku.JPG"
		},
		{
            name: 'Afterlife',
            lat: 54.3599358,
            lng: 18.653835,
            description: 'Cyberpunk themed bar',
            friendly: true,
            friendlyDescription: "It's a fairly new bar, and they allow cosplayers if you ask them beforehand. They require you to tag them in the photos.",
            legal: true,
            link: "https://www.instagram.com/afterlife_gdansk/"
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
		},
		{
			name: 'Train parking',
			lat: 54.3890585,
			lng: 18.634716,
			description: "A place with parked trains, nice scenery for military or industrial photos",
			friendly: false,
			friendlyDescription: "This is a private site which has monitoring. No reported issues so far, but not recommended",
			paid: false
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
			style: 'https://basemaps.cartocdn.com/gl/voyager-gl-style/style.json', // Example style
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

<div class="container">
	<div class="sidebar">
		<h2>Locations</h2>
		<div class="places-dropdown">
			<select on:change={(e) => flyToPlace(places[e.target.value])}>
				<option value="" disabled selected>Select a place</option>
				{#each places as place, i}
					<option value={i} selected={selectedPlace === place}>{place.name}</option>
				{/each}
			</select>
		</div>

		{#if selectedPlace}
			<div class="selected-place">
				<h2>Selected Location</h2>
				<PlaceInfoCard 
					place={selectedPlace} 
					onCenterMap={() => flyToPlace(selectedPlace)} 
				/>
			</div>
		{/if}
	</div>
	<div id="map" bind:this={mapContainer}></div>
</div>

<style>
	.container {
		display: flex;
		height: calc(100vh - 40px);
		width: 100vw;
		overflow: hidden;
	}

	.sidebar {
		width: 25%;
		min-width: 300px;
		height: calc(100vh - 40px);
		overflow-y: auto;
		box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
		padding: 15px;
        background-color: rgb(97, 163, 85);
	}

	h2 {
		margin-top: 0px;
	}

	#map {
		flex: 1;
		height: calc(100vh - 40px);
		position: relative;
	}

	.places-dropdown {
		margin-bottom: 20px;
	}

	.places-dropdown select {
		width: 100%;
		padding: 12px 15px;
		font-size: 16px;
		border-radius: 8px;
		border: 1px solid #ccc;
		background-color: white;
		cursor: pointer;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
		transition: all 0.3s ease;
		appearance: none;
		background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
		background-repeat: no-repeat;
		background-position: right 15px center;
		background-size: 16px;
	}

	.places-dropdown select:hover {
		border-color: #007bff;
	}

	.places-dropdown select:focus {
		outline: none;
		border-color: #007bff;
		box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
	}

	.places-dropdown option {
		font-size: 16px;
		padding: 10px;
	}

	.info-card {
		background-color: white;
		border-radius: 8px;
		padding: 15px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
		margin-bottom: 15px;
	}

	.info-card h3 {
		margin-top: 0;
		color: #333;
	}


	button {
		background-color: #007bff;
		color: white;
		border: none;
		padding: 8px 12px;
		border-radius: 4px;
		cursor: pointer;
		margin-top: 10px;
	}

	button:hover {
		background-color: #0056b3;
	}

	:global(.maplibregl-marker) {
		cursor: pointer;
		z-index: 10;
	}

	:global(.maplibregl-popup-content) {
		padding: 10px;
		border-radius: 5px;
	}
</style>
