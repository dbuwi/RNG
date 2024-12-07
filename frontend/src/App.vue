<template>
   
  <VApp class="bg-surface"> 
    <NavBar />

    <VMain class="ma-5" > 
      <RouterView v-slot="{ Component, route}"> 
        <transition :name="route.meta.transition || 'fade'" mode="out-in">
          <component :is="Component" />
        </transition>
      </RouterView>
    </VMain>

  </VApp>
  
</template>

<script setup>
  import { RouterView } from 'vue-router'
  import NavBar from '@/components/NavBar.vue';
 
</script>

<style>
 /* Slide right page transition */
 .slide-enter-active,
  .slide-leave-active {
  transition: opacity 0.5s, transform 0.5s;
  }

  .slide-enter-from,.slide-leave-to {
  opacity: 0; 
  }

  .slide-enter-to,.slide-leave-from {
  opacity: 1;
  transform: translateX(10px);
  }

  /* Fade page transition */
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.3s ease;
  }

  .fade-enter-from ,
  .fade-leave-to {
  opacity: 0;
  }


  /* Bounce */
  .bounce-enter-active {
    animation: bounce-in 0.5s;
  }
  .bounce-leave-active {
    animation: bounce-in 0.5s reverse;
  }
  @keyframes bounce-in {
    0% {
      transform: scale(0);
    }
    50% {
      transform: scale(1.25);
    }
    100% {
      transform: scale(1);
    }
  }

  /*
    Enter and leave animations can use different
    durations and timing functions.
  */
  .slide-fade-enter-active {
    transition: all 0.3s ease-out;
  }

  .slide-fade-leave-active {
    transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
  }

  .slide-fade-enter-from,
  .slide-fade-leave-to {
    transform: translateX(20px);
    opacity: 0;
  }
  </style>
