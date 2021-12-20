<template>
  <div class="container">
    <header class="jumbotron">
      <h3>
        <strong>{{id}}</strong> Profile
      </h3>
    </header>
    <p>
      <strong>Id:</strong>
      {{id}}
    </p>
    <p>
      <strong>id_type:</strong>
      {{id_type}}
    </p>

  </div>
</template>

<script>
import UserService from '../services/user.service';

export default {
  name: 'Profile',
  data() {
    return {
      id: '',
      id_type: ''
    };
  },
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
  },
  mounted() {
    UserService.getInfo().then(
      response => {
        this.content = response.data;
        this.id = response.data.id;
        this.id_type = response.data.id_type;
      },
      error => {
        this.content =
          (error.response && error.response.data) ||
          error.message ||
          error.toString();
      }
    );
    if (!this.currentUser) {
      this.$router.push('/login');
    }
  }
};
</script>