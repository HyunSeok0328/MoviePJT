<template>
<div>
  <div class="example-3d" v-if="myMovies2.length >= 1" >
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide 
        v-for="movie in myMovies2"
        :key="movie.movie.id"
        :style="{ backgroundImage : `url(https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${movie.movie.poster_path}`}"
      >
       <p>{{ movie.movie.title }}</p>
      </swiper-slide>
    </swiper>
  </div>
  <div class="example-3d" v-else >
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide 
        v-for="movie in myMovies" 
        :key="movie.movie.id"
        :style="{ backgroundImage : `url(https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${movie.movie.poster_path}`}"
      >
       <p>{{ movie.movie.title }}</p>
      </swiper-slide>
    </swiper>
    
  </div>
</div>
  
</template>

<script>
import axios from 'axios';
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'

export default {
  name: 'Recommend',
  components: {
    Swiper,
    SwiperSlide
  },
  data() {
    return {
      imgIndex: 1,
      myMovies: [],
      myMovies2: [],
      userId: '',
      swiperOption: {
        effect: 'coverflow',
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: 'auto',
        coverflowEffect: {
          rotate: 50,
          stretch: 0,
          depth: 100,
          modifier: 1,
          slideShadows : true
        },
        pagination: {
          el: '.swiper-pagination'
        }
      }
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
    getRecommendations: function(){
      axios({
      method: 'get',
      url: `http://127.0.0.1:8000/community/recommend/`,
      headers: this.setToken()
    })
      .then((res) => {
        this.myMovies = res.data
        console.log('추천1')

        console.log(res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
    getRecommendations2: function(){
      axios({
      method: 'get',
      url: `http://127.0.0.1:8000/community/${this.userId}/recommend2/`,
      headers: this.setToken()
    })
      .then((res) => {
        console.log('추천2')

        this.myMovies2 = res.data
        console.log(res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
     getUser: function(){
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/accounts/username/`,
          headers: this.setToken()
        })
          .then((res) => {
            this.userId = res.data.id
            console.log(res.data)
            this.getRecommendations2()
          })
          .catch(err => {
            console.log(err)
          })
      },
  },
  created: function(){
    this.getUser()
    this.getRecommendations()
  },
}
</script>

<style scoped>
.example-3d {
  width: 100%;
  height: 75vh;
  padding-top: 50px;
  padding-bottom: 50px;
}

.swiper {
  height: 100%;
  width: 100%;
}

.swiper-slide {
  display: flex;
  justify-content: center;
  align-items: end;
  width: 400px;
  height: 550px;
  text-align: center;
  font-weight: bold;
  background-size: 380px 480px;
  color: white;
  background-repeat: no-repeat;
}

</style>