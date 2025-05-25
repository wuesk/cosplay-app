<script lang="ts">
    export let color: string;
</script>

<span class="pill" style="background-color: {color}"><slot /></span>

<style>
    .pill {
      padding: 6px 12px;
      border-radius: 16px;
      font-size: 12px;
      color: white;
      display: inline-flex;
      align-items: center;
      margin: 2px 4px;
    }
</style>