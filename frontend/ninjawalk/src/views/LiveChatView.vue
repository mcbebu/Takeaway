<template>
  <h1>live</h1>
  <div id="livechat">
    <select-username
      v-if="!usernameAlreadySelected"
      @input="onUsernameSelection"
    />
    <chat v-else />
  </div>
</template>

<script>
import SelectUsername from "../components/liveChatComponents/SelectUsername.vue";
import Chat from "../components/liveChatComponents/Chat.vue";
import socket from "../services/socket.js";
export default {

}
</script>

<style>

</style>