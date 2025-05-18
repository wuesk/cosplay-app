<script>
	import '../app.css';
</script>

<div class="app">
	<main>
  		<slot />
	</main>
</div>

<style>
	.app, main {
		width: 100%;
		min-height: 100vh;
	}
</style>
