<script lang="ts">
	import FlagIcon from './FlagIcon.svelte';
	import type { ILocation } from '$lib/types/map';

	// Component props
	export let place: ILocation;
	export let onCenterMap: () => void;

	// Default image that will be used for all locations for now
	// In a real app, you would add an image property to the ILocation interface
	const defaultImage =
		'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Parque_Adam_Mickiewicz%2C_Oliwa%2C_Gdansk%2C_Polonia%2C_2013-05-21%2C_DD_04.jpg/1280px-Parque_Adam_Mickiewicz%2C_Oliwa%2C_Gdansk%2C_Polonia%2C_2013-05-21%2C_DD_04.jpg';

	function getDirectionsUrl(lat: number, lng: number, name: string): string {
		const encodedName = encodeURIComponent(name);
		return `https://www.google.com/maps/dir/?api=1&destination=${lat},${lng}&destination_place_id=${encodedName}`;
	}

	$: hasCoords = place.lat !== undefined && place.lng !== undefined;
</script>

<div class="info-card">
	<h3>{place.name}</h3>
	<div class="image-container">
		<img src={place.image || defaultImage} alt={place.name} />
	</div>
	<p>{place.description || 'No description available.'}</p>

	<h5>Venue attributes</h5>
	<div class="flags">
		<FlagIcon emoji="👘" flag={place.friendly} description={place.friendlyDescription} />
		<FlagIcon emoji="🤑" flag={place.paid} description={place.paidDescription} />
		<FlagIcon emoji="🅿️" flag={place.parking} description={place.parkingDescription} />
		<!--If it's friendly it's legal as well methinks-->
		<!--<FlagIcon emoji="👮" isLegal={place.legal} description={place.legalDescription}/>-->
	</div>
	
	<h5>Links</h5>
	<div class="links">
		{#if place.link}
			<a href={place.link} target="_blank" rel="noopener noreferrer">
				<span>ℹ️</span> Learn more
			</a>
		{/if}

		{#if hasCoords}
			<a
				href={getDirectionsUrl(place.lat, place.lng, place.name)}
				target="_blank"
				rel="noopener noreferrer"
				class="directions-link"
			>
				<span>📍</span> Get Directions (Google Maps)
			</a>
		{/if}
	</div>

	<button>Favourite</button>
	<button on:click={onCenterMap}>Center on Map</button>
</div>

<style>
	.info-card {
		background-color: rgb(118, 216, 141);
		border-radius: 8px;
		padding: 15px;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
		margin-bottom: 15px;
	}

	.info-card h3 {
		margin-top: 0;
		color: #333;
	}

	.image-container {
		margin-bottom: 15px;
		width: 100%;
		overflow: hidden;
		border-radius: 6px;
	}

	.image-container img {
		width: 100%;
		height: auto;
		display: block;
		transition: transform 0.3s ease;
	}

	.image-container img:hover {
		transform: scale(1.03);
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

	a {
		display: block;
		color: #007bff;
		text-decoration: none;
		margin-bottom: 10px;
	}

	a:hover {
		text-decoration: underline;
	}

	.flags {
		margin-top: 10px;
		display: flex;
		flex-wrap: wrap;
		margin-bottom: 10px;
	}

	h5 {
		margin-bottom: 0;
	}
</style>
