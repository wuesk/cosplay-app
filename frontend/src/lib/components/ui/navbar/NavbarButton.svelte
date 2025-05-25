<script lang="ts">
    export let item: any = {};
</script>

<button 
  class="w-12 h-12 flex items-center justify-center bg-stone-600 rounded-md shadow-md hover:shadow-lg transition-shadow duration-200 focus:outline-none focus:ring-2 focus:ring-blue-300 cursor-pointer"
  on:click={item.onClick} 
  aria-label={item.label}
>
    <span class="text-xl ">{item.icon}</span>
    <span class="sr-only">{item.label}</span>
    <div class="absolute left-full ml-2 px-2 py-1 bg-stone-800 text-stone-100 text-sm rounded opacity-0 group-hover:opacity-100 transition-opacity duration-200 whitespace-nowrap">
      {item.label}
    </div>
</button>