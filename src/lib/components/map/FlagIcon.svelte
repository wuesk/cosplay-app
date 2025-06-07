<script>
    export let emoji = "";
    export let flag = false;
    export let description = "";
</script>
  
<span class="flag-icon" class:tooltip-container={!!description}>
  {emoji}{#if flag}✅{:else}❌{/if}
  {#if description}
      <div class="tooltip-bubble">
          <p>{description}</p>
      </div>
  {/if}
</span>
  
<style>
  .flag-icon {
    margin-right: 12px;
    font-size: 30px;
    display: inline-flex;
    align-items: center;
  }
  
  .tooltip-container {
    position: relative;
    cursor: pointer;
  }
  
  .tooltip-bubble {
    visibility: hidden;
    position: absolute;
    bottom: 125%;
    left: 10%;
    transform: translateX(0);
    background-color: #333;
    color: white;
    text-align: center;
    border-radius: 8px;
    padding: 10px 15px;
    min-width: 180px;
    max-width: 250px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    opacity: 0;
    transition: opacity 0.3s, visibility 0.3s;
    z-index: 100;
  }
  
  .tooltip-bubble::after {
    content: "";
    position: absolute;
    top: 100%;
    left: 20px;
    margin-left: -8px;
    border-width: 8px;
    border-style: solid;
    border-color: #333 transparent transparent transparent;
  }
  
  .tooltip-container:hover .tooltip-bubble {
    visibility: visible;
    opacity: 1;
  }
  
  .tooltip-bubble p {
    margin: 0;
    font-size: 14px;
    line-height: 1.4;
  }
</style>