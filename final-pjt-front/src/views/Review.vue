<template>
  <div class="blog-container" v-if="review">
    <div class="blog-body">
      <div class="blog-title">
        <h1>{{ review.title }}</h1>
      </div>
      <div class="blog-summary">
        <p class="d-flex align-items-center justify-content-center">{{ review.content }}</p>
      </div>
    </div>
    <div class="blog-btn" v-if="review.user_id === user.id">
      <button class="review-btn me-3" @click="updateReview">UPDATE</button>
      <button class="review-btn" @click="deleteReview">DELETE</button>
    </div>
    <div class="blog-footer">
      <ul>
        <li class="published-date">작성일 : {{ review.created_at }}</li>
        <li class="published-date">수정일 : {{ review.updated_at }}</li>
      </ul>
    </div>
    
    <review-comment :review-id="reviewId"></review-comment>
  </div>
      
</template>

<script>
import axios from 'axios';
import ReviewComment from '@/components/community/ReviewComment'

export default {
  name: 'Review',
  components: {
    ReviewComment,
  },
  data: function(){
    return{
      review: null,
      reviewId: null,
      comment: false,
      user: [],
    }
  },
  created: function(){
     if (localStorage.getItem('jwt')){
      this.getReview()
      this.getUser()
    } else {
      this.$router.push({ name: 'Login' })
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
    getReview: function(){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/review/${this.$route.params.reviewId}/`,
        headers: this.setToken()
      })
        .then((res) => {
          this.reviewId = this.$route.params.reviewId
          this.review = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateReview: function(){
      this.$router.push({ name: 'UpdateReview', params: { reviewId: `${this.reviewId}`} })
    },
    deleteReview: function(){
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/community/review/${this.reviewId}/`,
        headers: this.setToken()
      })
        .then(() => {
          this.$router.push({ name: 'Community' })
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
          this.user = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    showComment: function(){
      this.comment = true
    }

  }
}

</script>

<style scoped>
.blog-body {
  margin: 0 auto;
  width: 80%;
  height: 50%
}

.blog-container {
  background: rgba(256, 256, 256, 0.1);
  border-radius: 5px;
  box-shadow: hsla(0, 0, 0, .2) 0 4px 2px -2px;
  font-family: "adelle-sans", sans-serif;
  font-weight: 100;
  margin: 48px auto;
  width: 80vw;
  padding-bottom: 48px;
  
  @media screen and (min-width: 480px) {
    width: 28rem;
  }
  @media screen and (min-width: 767px) {
    width: 40rem;
  }
  @media screen and (min-width: 959px) {
    width: 50rem;
  }
}
.blog-container a {
  color: #4d4dff;
  text-decoration: none;
  transition: .25s ease;
}
.blog-container a:hover{
  border-color: #ff4d4d;
  color: #ff4d4d;
}
.blog-title h1{
  padding: 10px;
  color: #fff;
  font-weight: 500;
  font-size: 30px;
  margin-bottom: 30px;
  border-bottom: solid 1px rgba(256, 256, 256, 0.3);
}
.blog-summary{
  height: 20vh;

}
.blog-summary p {
  color: lighten(#333, 10%);
  padding: 10px;
  height: 100%;
  margin: 0;
}
/* .blog-tags ul {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  list-style: none;
  padding-left: 0;
}
.blog-tags li + li {
  margin-left: .5rem;
} */
/* .blog-tags a {
  border: 1px solid lighten(#333, 40%);
  border-radius: 3px;
  color: lighten(#333, 40%);
  font-size: .75rem;
  height: 1.5rem;
  line-height: 1.5rem;
  letter-spacing: 1px;
  padding: 0 .5rem;
  text-align: center;
  text-transform: uppercase;
  white-space: nowrap;
  width: 5rem;
} */


.blog-footer {
  border-top: 1px solid lighten(#333, 70%);
  margin: 0 auto;
  padding-bottom: .125rem;
  width: 80%;
}
.blog-footer ul {
  list-style: none;
  padding-left: 0;
}
.blog-footer li:first-child {
  margin-right: auto;
}
.blog-footer li + li {
  margin-left: .5rem;
}
.blog-footer li {
  color: lighten(#333, 40%);
  font-size: .75rem;
  height: 1.5rem;
  letter-spacing: 1px;
  line-height: 1.5rem;
  text-align: center;
  text-transform: uppercase;
  position: relative;
  white-space: nowrap;
  text-align: right;
}
.blog-footer li a {
    color: lighten(#333, 40%);
}

.comments {
  margin-right: 1rem;
}
.published-date {
  border: 1px solid lighten(#333, 40%);
  border-radius: 3px;
  padding: 0 .5rem;
}
.numero {
  position: relative;
  top: -0.5rem;
}


.icon-bubble {
  fill: lighten(#333, 40%);
  height:24px;
  margin-right: .5rem;
  transition: .25s ease;
  width: 24px;
}

.icon-bubble:hover {
    fill: #ff4d4d;
}

.commentBtn{
  outline: none;
  border: none;
  background-color: transparent;
  color: #fff;
}

.review-btn{
  background-color: transparent;
  outline: none;
  border: 1px solid rgba(256, 256, 256, 0.7);
  border-radius: 8px;
  color:  rgba(256, 256, 256, 0.7);
  font-size: 12px;
}

.review-btn:hover{
  background-color: rgba(256, 256, 256, 0.3);
}
</style>