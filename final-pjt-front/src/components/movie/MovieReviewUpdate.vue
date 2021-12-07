<template>
  <div class="review-form">
    <div>
      <b-form-rating 
        v-model="rank" 
        variant="danger" 
        class="mb-2 star"
        show-value
        show-value-max
        no-border 
        size="lg"
      >
      </b-form-rating>
    </div>
    <div class="comment">
      <input 
        type="text" 
        v-model.trim="content"
        id="comment"
        @keyup.enter="updateRank"
        placeholder="감상평을 등록해주세요"
        class=""
      >
      <button @click="updateRank">수정</button>
    </div>
  </div>
</template>

<script>
import axios from'axios'

export default {
  name: 'MovieReviewUpdate',
  data: function(){
    return{
      rank: null,
      content: null,
    }
  },
  props: {
    movieId: String,
    reviewId: Number,
  },
  methods: {
    setToken: function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getRank: function(){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${this.movieId}/review/${this.reviewId}/`,
        headers: this.setToken()
      })
        .then((res) => {
          this.rank = res.data.rank,
          this.content = res.data.content
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateRank: function(){
      const rankItem = {
        rank: this.rank,
        content: this.content,
      }

      if (rankItem.content) {
        axios({
          method: 'put',
          url: `http://127.0.0.1:8000/community/${this.movieId}/review/${this.reviewId}/`,
          data: rankItem,
          headers: this.setToken()
        })
          .then(() => {
            this.$emit('update-review')
            this.$emit('get-avg')
            this.rank = null,
            this.content = null
          })
          .catch(err => {
            console.log(err)
          })
        }
    }
  },
  created: function(){
    this.getRank()
  }
}
</script>

<style scoped>
.review-form{
  width: 50vw;
}
input {
  border-radius: 6px;
  outline: none;
  background-color: transparent;
  border: 1px solid #fff;
  padding: 2px;
  width: 50%;
  height: 35px;
  margin-right: 20px;
  color: #fff;
}

.star{
  width: 50%;
  margin: 0 auto;
  background-color: transparent;
  color: white;
}
</style>