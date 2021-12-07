<template>
  <div>
    <hr>
    <div class="d-flex align-items-center ms-5">
      <b-icon icon="chat" font-scale="1" class="me-2"></b-icon>
      <span>Comments ({{comments.length}})</span>
    </div>
    <create-comment :review-id="reviewId" @new-comment="getComments"></create-comment>
    <ul class="comments">
      <li v-for="comment in comments" :key="comment.id" class="comment-item d-flex align-items-center">
        <div>
          <p class="comment-content">{{ comment.content }}</p>
          <p class="comment-time">작성일 : {{ comment.created_at }}</p>
        </div>
        <div v-if="comment.user_id === user.id" class="ms-auto me-3">
          <button class="delBtn" @click="deleteComment(comment)">X</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import CreateComment from '@/components/community/CreateComment'

export default {
  name: 'ReviewComment',
  components: {
    CreateComment,
  },
  data: function () {
    return {
      comments: [],
      user: [],
    }
  },
  props: {
    reviewId: String,
  },
  methods: {
    setToken: function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getComments: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/review/${this.reviewId}/comments/`,
        headers: this.setToken()
      })
        .then(res => {
          this.comments = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteComment: function(comment){
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/community/review/${this.reviewId}/comments/${comment.id}/`,
        headers: this.setToken()
      })
        .then(() => {
          this.getComments()
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
    }

  },
  created: function () {
    if (localStorage.getItem('jwt')){
      this.getComments()
      this.getUser()
    } else {
      this.$router.push({ name: 'Login' })
    }
  },
}
</script>

<style scoped>
.delBtn {
  border: none;
  background-color: transparent;
  color: #fff;
  width: 18px;
  height: 18px;
  font-size: 7px;
  padding: 0;
}
.comment-time{
  font-size: 10px;
  width: 100%;
  text-align: left;
  margin: 5px 0 0 0;
}
.comment-content{
  margin: 0;
}

.comment-item {
  width: 50%;
  margin: 20px auto;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
  border-radius: 10px;
  background-color: rgba(256, 256, 256, 0.03);
  border: 1px solid rgba(256, 256, 256, 0.5);
  text-align: left;
  padding: 10px;
}

.comments{
  padding: 0;
}
</style>