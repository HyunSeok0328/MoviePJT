<template>
  <div class="app">
    <div class="d-flex align-items-center nav">
      <router-link :to="{ name: 'Home' }" id="nav-home">NETFLEX</router-link>
      <div v-if="isLogin" class="ms-auto">
        <span>
          <input
            v-model.trim="searchKeyword"
            type="text" 
            @keyup.enter="moveToSearch"
            placeholder="Search"
            class="search-input"
          >
          <b-icon icon="search" class="nav-items" @click="moveToSearch"></b-icon> 
        </span>
        <router-link class="nav-items" :to="{ name: 'Community' }">Community</router-link> 
        <router-link class="nav-items" :to="{ name: 'Profile' }">Profile</router-link> 
        <router-link class="nav-items logout" to="#" @click.native="logout">Logout</router-link>
      </div>
      <div v-else class="ms-auto">
        <router-link class="nav-items" :to="{ name: 'Signup' }">Signup</router-link> 
        <router-link class="nav-items" :to="{ name: 'Login' }">Login</router-link> 
      </div>
     </div>
    <router-view class="content" @login="isLogin=true"/>
  </div>
</template>

<script>
// import axios from 'axios'
import Vue from 'vue';
import Carousel3d from 'vue-carousel-3d';
import { BootstrapVue, IconsPlugin, BootstrapVueIcons } from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(IconsPlugin)
Vue.use(Carousel3d);

export default ({
  name: 'App',
  data: function () {
    return {
      searchKeyword: '',
    }
  },
  created: function(){
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
    
    // DB 생성
    // axios({
    //   method: 'get',
    //   url: 'http://127.0.0.1:8000/movies/takegenres/',
    //   headers: this.setToken()
    // })
    //   .then(() => {
    //     axios({
    //       method: 'get',
    //       url: 'http://127.0.0.1:8000/movies/',
    //       headers: this.setToken()
    //       })
    //         .then(() => {
    //         })
    //         .catch(err => {
    //           console.log(err)
    //         })
    //     })
    //   .catch(err => {
    //     console.log(err)
    //   })
  },
  methods: {
    logout: function() {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    },
    setToken: function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    moveToSearch: function(){
      this.$router.push( { name: 'Search', query: {searchKeyword: `${this.searchKeyword}`} })
      this.searchKeyword = null
    }
  },

})

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Anton&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;500;700&display=swap');

.app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
  background:url("assets/background.jpg");
  background-size: cover;
  background-attachment: fixed;
  min-height: 120vh;
}

ul {
  list-style: none;
}

.nav {
  padding: 20px 15px;
  width: 100vw;
  /* position: fixed; */
  z-index: 1;
  /* background-color: #232324; */
  }

#nav-home {
  font-family: 'Anton', sans-serif;
  font-size: 50px;
  padding-left: 20px;
  color: #CC0000;
}

.nav-items {
  font-family: 'Open Sans', sans-serif;
  margin-right: 40px;
  font-size: 18px;
  cursor: pointer;
}

.nav-items:hover {
  color: #f72307;

}

.nav a {
  color: #fff;
  text-decoration: none;
}

.nav a.router-link-exact-active {
  color: #CC0000;
  
}

.content {
  padding-top: 40px;
}

.search-input{
  outline: none;
  border: none;
  background-color: transparent;
  border: 1px solid #fff;
  border-radius: 20px;
  padding: 2px 2px 2px 15px;
  width: 35%;
  height: 35px;
  color: #fff;
  font-family: 'Open Sans', sans-serif;
  font-weight: 500;
  margin-right: 10px;
}

.logout{
 
}

</style>
