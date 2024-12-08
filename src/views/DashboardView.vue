<script setup lang="ts">
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faSearch } from '@fortawesome/free-solid-svg-icons'
import Note from '@/components/Note.vue'
import { ref } from 'vue'

const url = ref('')
const filePath = ref('')
const HOST = import.meta.env.VITE_HOST_URL

const handleInput = (event) => {
  event.preventDefault()
  url.value = event.target.value
}

const downloadVideo = async () => {
  if (filePath.value) {
    try {
      const downloadUrl = `${HOST}/api/download`
      const res = await fetch(downloadUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          filename: filePath.value,
        }),
      })
      if (res.ok) {
        const blob = await res.blob()
        const url = URL.createObjectURL(blob)
        const link = document.createElement('a')

        link.href = url
        link.setAttribute('download', filePath.value)
        link.hidden = true

        document.body.appendChild(link)
        link.click()
        link.remove()
        URL.revokeObjectURL(url)
      } else {
        console.error('Error getting response from server.')
      }
    } catch (err) {
      console.error(err)
    }
  }
}

const handleSubmit = async (event) => {
  event.preventDefault()
  try {
    let res = await fetch(`${HOST}/api/video`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        url: url.value,
      }),
    })

    if (res.status === 200) {
      res = await res.json()
      console.log(res.data)
      filePath.value = res.data.downloadUrl
      console.log(filePath.value)
      await downloadVideo()
      filePath.value = ''
    }
  } catch (err) {
    console.log(err)
  }
}
</script>
<template>
  <div class="container">
    <h1 class="mb-5">Welcome to youtube video downloader.</h1>
    <div class="input-container mb-5">
      <FontAwesomeIcon :icon="faSearch" class="searchicon" />
      <input
        type="text"
        class="input"
        placeholder="Enter url of your video."
        @input="handleInput"
      />
      <button class="mb-5 submitBtn" @click="handleSubmit">
        <FontAwesomeIcon :icon="faSearch" class="searchicon" />
      </button>
    </div>
  </div>
  <Note class="note" />
</template>
<style scoped>
* {
  margin: 0;
  padding: 0;
}
.mb-5 {
  margin-bottom: 5px;
}
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 50vh;
  width: 50vw;
  background-color: white;
  color: black;
  padding: 10px;
  align-items: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.input-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
  border: 1px solid black;
  border-radius: 50px;
  width: 80%;
}
.searchicon {
  color: rgb(79, 79, 79);
  padding: 5px;
}
.input {
  flex: 1;
  padding: 5px;
  border: none;
  outline: none;
  font-size: large;
  font-family: monospace;
  color: rgb(54, 54, 54);
}
.submitBtn {
  position: relative;
  top: 2px;
  height: 40px;
  width: 40px;
  border-radius: 50%;
  outline: none;
  border: 1px solid rgb(82, 82, 82);
  box-shadow: 1px 1px 4px rgb(126, 126, 126);
  cursor: pointer;
}
.submitBtn:hover {
  animation: btnhoverEffect 250ms linear 200ms;
  animation-fill-mode: forwards;
}
.note {
  position: absolute;
  bottom: 20px;
  left: 35%;
}

@keyframes btnhoverEffect {
  0% {
    box-shadow: 0px 0px 4px rgb(126, 126, 126);
  }
  50% {
    box-shadow: 0px 0px 4px 1px rgb(126, 126, 126);
  }
  100% {
    box-shadow: 0px 0px 4px 2px rgb(126, 126, 126);
  }
}
</style>
