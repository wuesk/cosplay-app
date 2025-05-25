<script lang="ts">
	import FlagIcon from './FlagIcon.svelte';
	import type { ILocation } from '$lib/types/map';

	// Component props
	export let place: ILocation;
	export let onCenterMap: () => void;

	// Default image that will be used for all locations for now
	const defaultImage =
		'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Parque_Adam_Mickiewicz%2C_Oliwa%2C_Gdansk%2C_Polonia%2C_2013-05-21%2C_DD_04.jpg/1280px-Parque_Adam_Mickiewicz%2C_Oliwa%2C_Gdansk%2C_Polonia%2C_2013-05-21%2C_DD_04.jpg';

	function getDirectionsUrl(lat: number, lng: number, name: string): string {
		const encodedName = encodeURIComponent(name);
		return `https://www.google.com/maps/dir/?api=1&destination=${lat},${lng}&destination_place_id=${encodedName}`;
	}

	$: hasCoords = place.lat !== undefined && place.lng !== undefined;
</script>

<div class="bg-blue-950 rounded-lg p-4 shadow-md mb-4 text-blue-50">
	<h3 class="text-xl font-bold mb-3 text-blue-200">{place.name}</h3>
	
	<div class="mb-4 w-full overflow-hidden rounded-md">
		<img 
			src={place.image || defaultImage} 
			alt={place.name} 
			class="w-full h-auto block transition-transform duration-300 ease-in-out hover:scale-105"
		/>
	</div>
	
	<p class="mb-4">{place.description || 'No description available.'}</p>

	<!--<h5 class="text-lg font-semibold mb-1 text-blue-200">Venue attributes</h5>
	<div class="flex flex-wrap mb-4 gap-2">
		<FlagIcon emoji="👘" flag={place.friendly} description={place.friendlyDescription} />
		<FlagIcon emoji="🤑" flag={place.paid} description={place.paidDescription} />
		<FlagIcon emoji="🅿️" flag={place.parking} description={place.parkingDescription} />
	</div>-->
	
	<h5 class="text-lg font-semibold mb-1 text-blue-200">Links</h5>
	<div class="mb-4">
		{#if place.link}
			<a 
				href={place.link} 
				target="_blank" 
				rel="noopener noreferrer"
				class="block text-blue-300 hover:text-blue-100 hover:underline mb-2 transition-colors"
			>
				<span>ℹ️</span> Learn more
			</a>
		{/if}

		{#if hasCoords}
			<a
				href={getDirectionsUrl(place.lat, place.lng, place.name)}
				target="_blank"
				rel="noopener noreferrer"
				class="block text-blue-300 hover:text-blue-100 hover:underline mb-2 transition-colors"
			>
				<span>📍</span> Get Directions (Google Maps)
			</a>
		{/if}
	</div>

	<div class="flex gap-2 mt-2">
		<button class="bg-blue-800 hover:bg-blue-700 text-white py-2 px-4 rounded-md transition-colors shadow-sm">
			Favourite
		</button>
		<button 
			on:click={onCenterMap}
			class="bg-blue-800 hover:bg-blue-700 text-white py-2 px-4 rounded-md transition-colors shadow-sm"
		>
			Center on Map
		</button>
	</div>
</div>