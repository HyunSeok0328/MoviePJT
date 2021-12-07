<template>
  <div class="search">
    <b-container>
      <b-row class="mt-5" v-if="updateResult.length >= 1" >
        <b-col v-for="movie in updateResult" :key="movie.id" @click="moveToMovieDetail(movie)" class="search-item mb-4">
          <img 
            :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${movie.poster_path}`" 
            alt=""
            width="250px"
            height="350px"
          >
          <p class="mt-2">{{ movie.title }}</p>
        </b-col>
      </b-row>
      <div id="result" class="row mt-5" v-else>
        <p>검색 결과를 찾을 수 없습니다!</p>
      </div>
    </b-container>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Search',
  data: function() {
    return {
      movies: [],
    }
  },
  methods: {
    setToken: function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getMovie: function() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/home/`,
        headers: this.setToken()
      })
        .then((res) => {
          console.log(res)
          this.movies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    moveToMovieDetail: function(movie){
      console.log(movie.id)
      this.$router.push({ name: 'Movie', params: { movieId: `${movie.id}`} })
    }
  },
  computed: {
    updateResult: function() {
      let res = []
      for (const movie of this.movies){
        if (movie.title.includes(this.$route.query.searchKeyword)){
          res.push(movie)
        } else if (movie.overview.includes(this.$route.query.searchKeyword)){
          res.push(movie)
        } else if (movie.release_date.includes(this.$route.query.searchKeyword)){
          res.push(movie)
        } else if (movie.actorname.includes(this.$route.query.searchKeyword)){
          res.push(movie)
        } else if (movie.genrename.includes(this.$route.query.searchKeyword)){
          res.push(movie)
        }
      }
      return res
    },
  },
  created: function () {
    if (localStorage.getItem('jwt')){
      this.getMovie()
    } else {
      this.$router.push({ name: 'Login' })
    }
  },
}
</script>

<style scoped>
.search-item{
  cursor: pointer;
}

input {
  outline: none;
  border: none;
  background-color: transparent;
  border-bottom: 1px solid #fff;
  padding: 2px 2px 2px 15px;
  width: 15%;
  height: 35px;
  color: #fff;
  font-family: 'Open Sans', sans-serif;
  font-weight: 500;
  margin-right: 10px;
}

.search-btn {
  background-color: transparent;
  outline: none;
  border: none;
  color: white;
  font-size: 20px;
}

.search-item:hover{
  -webkit-transition: all 0.2s ease-in-out; 
  -moz-transition: all 0.2s ease-in-out; 
  -o-transition: all 0.2s ease-in-out; 
  transition: all 0.2s ease-in-out;
  z-index: 3;
  transform: scale(1.02) translateZ(0);
}

</style>