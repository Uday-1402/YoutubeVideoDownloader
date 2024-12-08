<script setup lang="ts">
import { ref } from 'vue'

// const file_handle = ref('')

const setFileHandle = async () => {
  try {
    console.log('Demo')
  } catch (err) {
    console.log(err)
  }
}
</script>

<template>
  <div id="main-container">
    Hello World.. This is the demo page.. Working with vue for the first time..
  </div>
  <div class="block1" :class="{ redColor: 1 }"></div>
  <button @click="setFileHandle">Select Directory</button>
</template>

<style>
#main-container {
  margin: 0;
  padding: 0;
  height: 50vh;
  width: 50vw;
  background-color: rgb(0, 100, 100);
  color: yellow;
  font-weight: bolder;
  text-align: center;
}
.block1 {
  margin: 20px;
  height: 100px;
  width: 100px;
  border: 1px solid green;
}
.redColor {
  background-color: red;
}
.blueColor {
  background-color: blue;
}
</style>
