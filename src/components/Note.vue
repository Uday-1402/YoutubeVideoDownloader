<script setup lang="ts">
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faCircleInfo } from '@fortawesome/free-solid-svg-icons'
</script>

<template>
  <div class="note-container">
    <FontAwesomeIcon :icon="faCircleInfo" class="info-icon" />
    <p class="msg">Only public/unrestricted videos can be downloaded currently.</p>
  </div>
</template>

<style scoped>
.note-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: max-content;
  padding: 10px;
  border: 1px solid rgb(182, 182, 182);
  border-radius: 50px;
}
.msg {
  flex: 1;
}
.info-icon {
  margin: 5px;
  color: red;
}
</style>
