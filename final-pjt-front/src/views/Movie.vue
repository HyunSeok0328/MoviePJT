<template>
  <div class="d-flex">
    <div class="card" :style="{ backgroundImage : `url(${posterUrl})`}">
      <div class="card__inner">
        <main class="card__body">
          <div class="card__info">
            <h1 class="card__title">{{ movie.title }}</h1>
            <p class="card__slug">{{movie.overview}}</p>
            <div class="red-icons">
              <button class="card__btn" @click="clickExplore">Explore</button>
              <div class="card__rating">
                {{ movie.vote_average }}
              </div>
            </div>
          </div>
        </main>
        <footer class="card__footer">
          <ul class="list list--info">
            <li>{{ movie.release_date }} 개봉</li>
            <li>{{ movie.genrename }}</li>
          </ul>
        </footer>
      </div>
    </div>
    <div class="review-comment d-flex flex-column pt-2">
      <div v-if="isLogin">
        <movie-review-update 
          :movie-id="movieId" 
          :review-id="reviewId" 
          @update-review="getDetailReview"
          @get-avg="getAvg"
          v-if="update"
          class="review-form"
        >
        
        </movie-review-update>
        <movie-review-create 
          v-else 
          :movie-id="movieId" 
          @new-review="getDetailReview"
          @get-avg="getAvg"
          class="review-form"
          @login="isLogin=true"
        >
        </movie-review-create>
      </div>
      <p v-else>평점을 남기려면 로그인하세요.</p>
      <br>
      <p>리뷰 평점: {{avg}}</p>

      <ul class="reviews">
        <li v-for="review in detailReview" :key="review.id" class="p-2 my-3 each-review">
          <div class="movie-review d-flex justify-content-between">
            <div>
              <p v-if="review.rank === '5'" class="stars">★★★★★ <span class="review-score">{{review.rank}}</span></p>
              <p v-if="review.rank === '4'" class="stars">★★★★ <span class="review-score">{{review.rank}}</span></p>
              <p v-if="review.rank === '3'" class="stars">★★★ <span class="review-score">{{review.rank}}</span></p>
              <p v-if="review.rank === '2'" class="stars">★★ <span class="review-score">{{review.rank}}</span></p>
              <p v-if="review.rank === '1'" class="stars">★ <span class="review-score">{{review.rank}}</span></p>
              
              <p>{{ review.content }}</p>
              <p class="review-username">{{ review.user.username }}</p>
            </div>
            <div v-if="review.user_id === user.id">
              <button class="updateBtn" @click="updateDetailReview(review)">
                <b-icon icon="brush" >수정</b-icon>
              </button>
              <button class="delBtn" @click="deleteDetailReview(review)">X</button>
            </div>
          </div>
        </li>
      </ul>
      </div>
  </div>

</template>

<script>
import axios from 'axios';
import MovieReviewCreate from '@/components/movie/MovieReviewCreate'
import MovieReviewUpdate from '@/components/movie/MovieReviewUpdate'

export default {
  name: 'Movie',
  components: {
    MovieReviewCreate,
    MovieReviewUpdate,
    
  },
  data: function(){
    return{
      movie: '',
      movieId: '',
      posterUrl: '',
      detailReview: null,
      user: [],
      update: false,
      reviewId: '',
      avg: 0,
    }
  },
  created: function() {
    this.getMovie()
    this.getDetailReview()
    this.getUser()
    this.getAvg()
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
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
    getMovie: function(){
      axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${this.$route.params.movieId}/`,
    })
      .then((res) => {
        this.movieId = this.$route.params.movieId
        this.movie = res.data[0]
        this.posterUrl = 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/' + res.data[0].poster_path
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
          console.log(res)
          this.user = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    getDetailReview: function(){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${this.$route.params.movieId}/review/`,
      })
        .then((res) => {
          this.detailReview = res.data.reverse()
          this.update = false
        })
        .catch(err => {
          console.log(err)
        })  
    },
    getAvg: function() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${this.$route.params.movieId}/avg/`,
      })
        .then((res) => {
          this.avg = res.data
          console.log(res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteDetailReview: function(review){
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/community/${this.$route.params.movieId}/review/${review.id}/`,
        headers: this.setToken()
      })
        .then(() => {
          this.getDetailReview()
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateDetailReview: function(review){
      this.update = true
      this.reviewId = review.id
    },
    clickExplore: function(){
      window.open(`https://google.com/search?q=${this.movie.title}`, "_blank");
    }
  },
}
</script>

<style scoped>
.delBtn {
  border: 1px solid #f72307;
  border-radius: 4px;
  background-color: transparent;
  color: #f72307;
  width: 18px;
  height: 18px;
  font-size: 7px;
  padding: 0;
}
ul {
  padding: 0;
  width: 50vw;
  margin: 0 auto;
}
li {
  text-align: left;
}
.review-form{
  margin: 0 auto;
}

@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/css/font-awesome.min.css');
html,
body,
.wrapper {
  width: 100vw;
}

html {
  font-size: 16px;
}

body {
  font-size: 100%;
  font-family: "Roboto", Arial, Verdana, sans-serif;
  background: #eee;
}

ul {
  padding: 0;
  margin: 0;
  list-style-type: none;
}

.card {
  position: relative;
  margin-right: auto;
  margin-left: 7rem;
  margin-bottom: 10rem;
  overflow: hidden;
  width: 55vw;
  height: 90vh;
  background-color:  rgba(0, 0, 0, 0.4);
  background-repeat: no-repeat;
  background-size: 70% 100%;
  border-radius: 0.6rem;
  box-shadow: 0 20px 30px rgba(0, 0, 0, 0.3), 0 25px 25px rgba(0, 0, 0, 0.3);
}
.card:after {
  content: "";
  position: absolute;
  z-index: 1;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
            to right,
            rgba(0, 0, 0, 0) 10%,
            rgba(0, 0, 0, 0.5) 50%,
            rgba(0, 0, 0, 1) 100%
          )
}

.card__inner {
  position: relative;
  z-index: 2;
  height: 100%;
}

.list {
  display: flex;
}

.list--nav {
  justify-content: space-around;
}
.list--nav li {
  width: calc(100%/3);
  background: #111;
  transition: all 0.2s cubic-bezier(0.4, 0, 1, 1);
}
.list--nav li:focus, .list--nav li:hover {
  background: #333;
}
.list--nav li:first-of-type {
  background: #292929;
}
.list--nav a {
  display: block;
  padding-top: 0.85rem;
  padding-bottom: 0.85rem;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.125rem;
  text-align: center;
  text-transform: uppercase;
  text-decoration: none;
  color: #fff;
}

.card__body {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 100%;
}

.card__info,
.card__footer {
  color: #fff;
  z-index: 5;
}

.card__info {
  position: relative;
  padding-right: 1.25rem;
  float: right;
  width: 45%;
}

.card__title {
  margin-bottom: 1rem;
  font-size: 2rem;
  font-weight: 600;
  text-transform: uppercase;
}

.card__slug {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
  word-wrap:break-word; 
  line-height: 2em;
  height: 10rem;
  color: rgba(255, 255, 255, 0.95);
}

.card__btn {
  display: inline-block;
  padding: 0.65rem 1.5rem;
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.0625rem;
  text-transform: uppercase;
  color: #fff;
  background: #c62828;
  border: 0;
  border-radius: 2.1875rem;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
  transition: all 0.2s cubic-bezier(0.4, 0, 1, 1);
}
.card__btn:focus, .card__btn:hover {
  color: #fff;
  background: #dc5454;
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
}

.card__rating {
  display: inline-block;
  position: relative;
  padding: 1rem;
  margin-left: 3rem;
  color: #fff;
  border-radius: 50%;
  border: 3px solid #c62828;
  
}
.card__rating:before {
  content: "";
  position: absolute;
  z-index: 2;
  top: -5px;
  left: 0;
  width: 50%;
  height: 20px;
  background: #000;
}

footer {
  position: absolute;
  bottom: 0;
  padding-top: 1rem;
  padding-right: 1.25rem;
  padding-bottom: 1rem;
  width: 100%;
}

.list--info {
  width: 50%;
  justify-content: end;
  margin-left: auto;
}
.list--info li {
  font-size: 0.85rem;
  margin-right: 16px;
}

.delBtn {
  border: 1px solid #f72307;
  border-radius: 4px;
  background-color: transparent;
  color: #f72307;
  width: 18px;
  height: 18px;
  font-size: 7px;
  padding: 0;
}

.updateBtn {
  border: 1px solid #f72307;
  border-radius: 4px;
  background-color: transparent;
  color: #f72307;
  width: 18px;
  height: 18px;
  font-size: 7px;
  padding: 0;
  margin-right: 4px;
}

.review-comment {
  width: 45vw;
  margin-right: 70px;
}
.reviews {
  padding: 0;
  width: 50vw;
}
.each-review {
  width: 70%;
  margin: 0 auto;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
  border-radius: 10px;
  background-color: rgba(256, 256, 256, 0.03);
  text-align: left;
}
.stars {
  color: red;
}
.review-username{
  font-size: 12px;
  
}
.review-score {
  font-size: 11px;
  color: rgba(256, 256, 256, 0.5);
}
.red-icons{
  margin-top: 70px;
}



</style>