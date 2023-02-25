<template>
<h1>Live Chat</h1>
<div class="container-fluid">


      </div>

</template>

<script>

export default {
name: 'LiveChatView',
}

</script>

<style>

</style>
<template>
    <div id="app">
      <select-username
        v-if="!usernameAlreadySelected"
        @input="onUsernameSelection"
      />
      <chat v-else />
    </div>
  </template>
  
  <script>
  import SelectUsername from "../components/socketIoComponents/SelectUsername";
  import Chat from "../components/socketIoComponents/Chat";
  import socket from "../socket";
  
  export default {
    name: "LiveChatView",
    components: {
      Chat,
      SelectUsername,
    },
    data() {
      return {
        usernameAlreadySelected: false,
      };
    },
    methods: {
      onUsernameSelection(username) {
        this.usernameAlreadySelected = true;
        socket.auth = { username };
        socket.connect();
      },
    },
    created() {
      const sessionID = localStorage.getItem("sessionID");
  
      if (sessionID) {
        this.usernameAlreadySelected = true;
        socket.auth = { sessionID };
        socket.connect();
      }
  
      socket.on("session", ({ sessionID, userID }) => {
        // attach the session ID to the next reconnection attempts
        socket.auth = { sessionID };
        // store it in the localStorage
        localStorage.setItem("sessionID", sessionID);
        // save the ID of the user
        socket.userID = userID;
      });
  
      socket.on("connect_error", (err) => {
        if (err.message === "invalid username") {
          this.usernameAlreadySelected = false;
        }
      });
    },
    destroyed() {
      socket.off("connect_error");
    },
  };
  </script>
  
  <style>
  body {
    margin: 0;
  }
  
  @font-face {
    font-family: Lato;
    src: url("../public/fonts/Lato-Regular.ttf");
  }
  
  #LiveChatView {
    font-family: Lato, Arial, sans-serif;
    font-size: 14px;
  }
  </style>
  