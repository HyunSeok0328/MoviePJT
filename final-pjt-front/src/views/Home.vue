<template>
  <b-container>
    <b-row>
      <b-col cols="4" v-for="movie in $store.state.movies" :key="movie.id">
        <div class="card" @click="moveToMovie(movie)">
          <div class="card-image">
            <img 
              :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${movie.poster_path}`" 
              alt=""
              class="card-image"
            >
          </div>
          <div class="card-text my-2">
            <div class="date">{{movie.release_date}}</div>
            <p>{{ movie.genrename }}</p>
            <h2>{{ movie.title }}</h2>
          </div>
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
// import axios from 'axios'
// import { mapState } from 'vuex'

export default {
  name: 'Home',
  data() {
      return {
        modalShow: false
      }
  },
  methods: {
    moveToMovie: function(movie){
      this.$router.push({ name: 'Movie', params: { movieId: `${movie.id}`} })
    }
  },
  created: function(){
    this.$store.dispatch('LoadMovieCards')
    // this.$store.dispatch('LoadUserInfo')
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&display=swap');

.card {
  border-radius: 18px;
  background: #1d1d1d;
  color:white;
  box-shadow: 5px 5px 20px rgba(0,0,0,0.9);
  font-family: roboto sans-serif;
  text-align: justify;
  cursor: pointer;
  margin:20px;
}
.card-image {
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  width: 100%;
  height: 100%;
}
.card-text {
  grid-area: text;
  margin: 20px;
  transform: translateZ(30px);
}
.card-text .date {
  color: #CC0000;
  font-size:13px;
  font-weight: bold;
  margin-bottom: 6px;
}
.card-text p {
  color: grey;
  font-size:14px;
  font-weight: 300;
}
.card-text h2 {
  margin-top:0px;
  font-size: 1.5rem;
  font-weight: 500;

}

.card:hover{
  -webkit-transition: all 0.42s ease-in-out; 
  -moz-transition: all 0.42s ease-in-out; 
  -o-transition: all 0.42s ease-in-out; 
  transition: all 0.42s ease-in-out;
  z-index: 3;
  transform: scale(1.08) translateZ(0);
}
</style>
