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
    <!-- <div>
      <label for="rank">별점을 선택해주세요:</label>
      <select v-model="rank">
        <option disabled value="">Please select one</option>
        <option>★</option>
        <option>★★</option>
        <option>★★★</option>
        <option>★★★★</option>
        <option>★★★★★</option>
      </select>
    </div> -->
    <div class="comment">
      <input 
        type="text" 
        v-model.trim="content"
        id="comment"
        @keyup.enter="createRank"
        placeholder="감상평을 등록해주세요"
      >
      <b-button variant="outline-light" size="sm" @click="createRank">
        <b-icon icon="check2"></b-icon>
      </b-button>
    </div>
  </div>
</template>

<script>
import axios from'axios'

export default {
  name: 'MovieReviewCreate',
  data: function(){
    return{
      rank: null,
      content: null,
    }
  },
  props: {
    movieId: String,
  },
  methods: {
    setToken: function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createRank: function(){
      const rankItem = {
        rank: this.rank,
        content: this.content,
      }

      if (rankItem.content) {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/community/${this.movieId}/review/`,
          data: rankItem,
          headers: this.setToken()
        })
          .then(() => {
            this.$emit('new-review')
            this.$emit('get-avg')
            this.rank = null,
            this.content = null
          })
          .catch(() => {
            alert('별점과 감상평 모두 등록해주세요!')
          })
        }
    }
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