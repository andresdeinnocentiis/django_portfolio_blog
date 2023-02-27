<template>
    <div class="star-rating">
      <span :style="{'color':color}" v-for="i in 5" :key="i" :data-index="i" @mousemove="handleMouseMove" @mouseleave="handleMouseLeave" @click="handleClick">
        <font-awesome-icon icon="fa-regular fa-star-half-stroke halfStar star-icon" v-if="(value == (i -1) + 0.5) && value > 0" />
        <font-awesome-icon icon="fa-solid fa-star fullStar star-icon" v-else-if="value >= i" />
        <font-awesome-icon icon="fa-regular fa-star emptyStar star-icon" v-else />
      </span>
    </div>
  </template>
  
  <script setup>
  import { ref, defineEmits } from 'vue';
  
  const value = ref(0);
  const clicked = ref(false)

  const starWidth = ref(0)

  const props = defineProps({
    color: String,
  })

  // I define the emit event for updating this value and passing it up to its parent component
  const emits = defineEmits(["update:value"]);
  
  const handleMouseMove = (event) => {

    const element = document.querySelector('.star-rating');

    const elementLength = element.offsetWidth;

    const index = event.currentTarget.dataset.index;

    starWidth.value = elementLength / 5;

    const offsetX = event.offsetX;

    if (offsetX >= (starWidth.value / 2)) {
      value.value = index
    } else if (offsetX < (starWidth.value / 2)) {
      value.value = index - 0.5
    }

  };
  
  const handleMouseLeave = () => {
    if (!clicked.value) {
      value.value = 0;
    }
  };

  const handleClick = () => {
    clicked.value = !clicked.value
    if (!clicked.value) {
      value.value = 0
    }
    // Here I emit an event to update the value on the parent component so that I can get the value and do whatever I need with it
    emits("update:value", value.value)
  }
  </script>

  