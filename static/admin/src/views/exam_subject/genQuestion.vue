<template>
  <el-main class="bg edit_wrap gen">
    <el-form ref="form" :model="form" status-icon label-width="70px">
      <el-row class="row_e">
        <el-col :xs="24" :sm="24" :lg="24" class="el_form_item_warp">
          <el-form-item label="单选题数目" prop="danxuanti_count">
            <el-input-number v-model="danxuanti_count"></el-input-number>
          </el-form-item>
        </el-col>

        <el-col :xs="24" :sm="24" :lg="24" class="el_form_item_warp">
          <el-form-item label="多选题数目" prop="duoxuanti_count">
            <el-input-number v-model="duoxuanti_count"></el-input-number>
          </el-form-item>
        </el-col>

        <el-col :xs="24" :sm="24" :lg="24" class="el_form_item_warp">
          <el-form-item label="判断题数目" prop="panduanti_count">
            <el-input-number v-model="panduanti_count"></el-input-number>
          </el-form-item>
        </el-col>

        <el-col :xs="24" :sm="24" :lg="24" class="el_form_item_warp">
          <el-form-item label="填空题数目" prop="tiankongti_count">
            <el-input-number v-model="tiankongti_count"></el-input-number>
          </el-form-item>
        </el-col>

        <el-col :xs="24" :sm="24" :lg="24" class="el_form_item_warp">
          <el-form-item label="主观题数目" prop="zhuguanti_count">
            <el-input-number v-model="zhuguanti_count"></el-input-number>
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
      field: "exam_id",
      url_add: "~/api/subject_exam_question/add?",
      url_del: "~/api/subject_exam_question/del?",
      url_exam_question_add: "~/api/subject_exam_question/add?",
      query: {
        exam_id: 0,
      },

      form: {
        exam_id: 0,
        subject_name: this.$route.query.subject_name,
      },
      list_subject: [],
      exam_question_list: [],
      danxuanti_count: 0,
      duoxuanti_count: 0,
      panduanti_count: 0,
      tiankongti_count: 0,
      zhuguanti_count: 0,
    };
  },
  methods: {
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
    submit_exam_question() {},
    /**
     * 自动生成试题库
     */
    async gen_question_list() {
      let _this = this;
      //题目类型
      let typeArry = [
        { type: "单选题" },
        { type: "多选题" },
        { type: "判断题" },
        { type: "填空题" },
        { type: "主观题" },
      ];
      //题目类型条数
      let sizeArry = [
        this.danxuanti_count,
        this.duoxuanti_count,
        this.panduanti_count,
        this.tiankongti_count,
        this.zhuguanti_count,
      ];

      this.$get(_this.url_del, { exam_id: this.query.exam_id }).then((res) => {
        // console.log(res);
      });

      let order = 0;
      for (let i = 0; i < typeArry.length; i++) {
        let query = typeArry[i];
        let size = sizeArry[i];

        //清空数组
        this.exam_question_list.splice(0, this.exam_question_list.length);

        query.subject_name = this.form.subject_name;
        //从试卷题库中获取题库列表
        await this.$get("~/api/exam_question_database/get_list?", query).then(
          (json) => {
            if (json.result) {
              //打乱顺序
              let list = json.result.list.sort(() => Math.random() - 0.5);

              if (size > list.length) {
                size = list.length;
              }
              for (let j = 0; j < size; j++) {
                order++;
                let exam = list[j];

                this.$delete(exam, "update_time");
                this.$delete(exam, "create_time");
                this.$delete(exam, "exam_question_id");

                exam.exam_id = this.query.exam_id;
                exam.subject_name = this.form.subject_name;
                exam.question_order = order;

                //添加到试卷题库中
                this.$post(
                  this.url_exam_question_add,
                  exam,
                  function (json, status) {
                    console.log("提交结果：", json);
                  }
                );
              }
            } else if (json.error) {
              console.error(json.error);
            }
          }
        );
      }
    },

    submit_main() {
      this.gen_question_list();
      this.events("submit_after", {}, null);
    },
  },
  created() {
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
