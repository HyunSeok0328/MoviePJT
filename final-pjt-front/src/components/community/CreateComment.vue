<template>
  <div class="d-flex align-items-center justify-content-center mb-4">
      <input 
        type="text" 
        v-model.trim="content"
        id="comment"
        @keyup.enter="createComment"
        placeholder="댓글을 작성하세요"
      >
      <b-button variant="outline-light" size="sm" @click="createComment">
        <b-icon icon="check2"></b-icon>
      </b-button>
  </div>
</template>

<script>
import axios from'axios'

export default {
  name: 'CreateComment',
  data: function () {
    return {
      content: null,
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
    createComment: function () {
      const commentItem = {
        content: this.content,
        review: this.reviewId,
      }

      if (commentItem.content) {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/community/review/${this.reviewId}/comments/`,
          data: commentItem,
          headers: this.setToken()
        })
          .then(() => {
            this.$emit('new-comment')
            this.content = null
          })
          .catch(err => {
            console.log(err)
          })
        }
    },
  }
}
</script>

<style scoped>
input {
  outline: none;
  border: none;
  background-color: transparent;
  border-bottom: 1px solid #fff;
  padding: 2px;
  width: 30%;
  height: 35px;
  margin-right: 20px;
  color: #fff;
}

</style>