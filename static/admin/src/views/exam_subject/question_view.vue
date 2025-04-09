<template>
  <el-main class="bg edit_wrap question_edit_wrap">
    <el-form ref="form" :model="form" status-icon label-width="70px">
      <el-row class="row_e">
        <el-col :xs="24" :sm="24" :lg="24" class="el_form_item_warp">
          <el-form-item label="科目" prop="subject_name">
            <el-input v-model="form.subject_name" :disabled="true"></el-input>
          </el-form-item>
        </el-col>

        <el-col :xs="24" :sm="24" :lg="24" class="el_form_item_warp">
          <el-form-item label="类型" prop="type">
            <el-select v-model="form.type">
              <el-option value="" label="">请选择</el-option>
              <el-option value="单选题" label="单选题">单选题</el-option>
              <el-option value="多选题" label="多选题">多选题</el-option>
              <el-option value="判断题" label="判断题">判断题</el-option>
              <el-option value="填空题" label="填空题">填空题</el-option>
              <el-option value="主观题" label="主观题">主观题</el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :xs="24" :sm="24" :lg="24" class="el_form_item_warp">
          <el-form-item label="题目" prop="title">
            <el-input v-model="form.title" placeholder="请输入题目"></el-input>
          </el-form-item>
        </el-col>

        <el-col :xs="24" :sm="24" :lg="24" class="el_form_item_warp">
          <el-form-item label="选项" prop="question_item">
            <el-input
              type="textarea"
              v-model="form.question_item"
              placeholder="输入问题选项，如：
A.正确
B.错误"
            >
            </el-input>
          </el-form-item>
        </el-col>

        <el-col :xs="24" :sm="24" :lg="24" class="el_form_item_warp">
          <el-form-item label="参考答案" prop="answer">
            <el-input
              v-model="form.answer"
              placeholder="请输入参考答案，如：A.正确,多个选项用|分隔"
            ></el-input>
          </el-form-item>
        </el-col>

        <el-col :xs="24" :sm="24" :lg="24" class="el_form_item_warp">
          <el-form-item label="分值" prop="score">
            <el-input-number v-model="form.score"></el-input-number>
          </el-form-item>
        </el-col>

        <el-col :xs="24" :sm="24" :lg="24" class="el_form_item_warp">
          <el-form-item label="排序" prop="question_order">
            <el-input-number v-model="form.question_order"></el-input-number>
          </el-form-item>
        </el-col>

       
      </el-row>
      <el-col :xs="24" :sm="24" :lg="24" class="el_form_btn_warp">
          <el-form-item>
            <el-col
              :xs="24"
              :sm="24"
              :lg="12"
              class="el_form_btn el_form_btn_1"
            >
              <el-button
                style="width: 100%; float: left"
                type="primary"
                @click="submit()"
                >提交
              </el-button>
            </el-col>
            <el-col
              :xs="24"
              :sm="24"
              :lg="12"
              class="el_form_btn el_form_btn_2"
            >
              <el-button style="width: 100%; float: right" @click="cancel()"
                >取消</el-button
              >
            </el-col>
          </el-form-item>
        </el-col>
    </el-form>
  </el-main>
</template>

<script>
import mixin from "@/mixins/page.js";

export default {
  mixins: [mixin],
  data() {
    return {
      field: "exam_question_id",
      url_add: "~/api/subject_exam_question/add?",
      url_set: "~/api/subject_exam_question/set?",
      url_get_obj: "~/api/subject_exam_question/get_obj?",
      url_upload: "~/api/subject_exam_question/upload?",

      query: {
        exam_question_id: 0,
      },

      form: {
        exam_question_id: 0,
        type: "",
        subject_name: this.$route.query.subject_name,
        title: "",
        question_item: "",
        answer: "",
        score: 0,
        question_order: 0,
        exam_id: 0,
      },
      list_subject: [],
    };
  },
  methods: {
    init_exam_id() {
      let exam_id = this.$route.query.exam_id;
      if (exam_id) {
        this.form.exam_id = exam_id;
      }
    },

    /**
     * 获取科目列表
     */
    async get_subject_list() {
      var json = await this.$get("~/api/subject/get_list?");
      if (json.result) {
        this.list_subject = json.result.list;
      } else if (json.error) {
        console.error(json.error);
      }
    },

    /**
     * 创建一个试题库
     */
    create_exam_database() {
      let obj = {
        exam_question_id: this.form.exam_question_id,
        type: this.form.type,
        subject_name: this.form.subject_name,
        title: this.form.title,
        question_item: this.form.question_item,
        answer: this.form.answer,
        score: this.form.score,
      };
      this.$post(this.url_add_question_database, obj, function (json, status) {
        console.log("提交结果：", json);
      });
    },

    submit_before() {
      this.create_exam_database();
    },
  },

  created() {
    this.init_exam_id();
    this.get_subject_list();
  },
};
</script>

<style>
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}

.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}

.avatar {
  width: 178px;
  height: 178px;
  display: block;
}

.el-row {
  justify-content: start;
  justify-items: start;
  align-items: start;
  align-content: flex-start;
}
</style>
