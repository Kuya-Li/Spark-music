<template>
  <el-main class="bg table_wrap subject_question">
    <el-form
      label-position="right"
      :model="query"
      class="form p_4"
      label-width="120"
    >
      <el-row class="rows row1">
        <el-col :xs="24" :sm="24" :lg="8" class="el_form_search_wrap">
          <el-form-item label="题目名称">
            <el-input v-model="query.title"></el-input>
          </el-form-item>
        </el-col>

        <el-col :xs="24" :sm="24" :lg="8" class="el_form_search_wrap">
          <el-form-item label="题目类型">
            <el-select v-model="query.type">
              <el-option value="" label="">请选择</el-option>
              <el-option value="单选题" label="单选题">单选题</el-option>
              <el-option value="多选题" label="多选题">多选题</el-option>
              <el-option value="判断题" label="判断题">判断题</el-option>
              <el-option value="填空题" label="填空题">填空题</el-option>
              <el-option value="主观题" label="主观题">主观题</el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row class="rows row2">
          <el-col :xs="24" :sm="24" :lg="24" class="search_btn_wrap">
          <el-col :xs="24" :sm="12" :lg="12" class="search_btn_1 btns">
           
              <el-button
                type="primary"
                @click="search()"
                class="search_btn_find"
                >查询</el-button
              >
              <el-button @click="reset()" class="search_btn_reset"
                >重置</el-button
              >
              <el-button
                v-if="
                  user_group == '管理员' || $check_action('/exam/table', 'del')
                "
                class="float-right search_btn_del"
                type="danger"
                @click="delInfo()"
                >删除</el-button
              >
              <!-- <router-link
                v-if="
                  user_group == '管理员' || $check_action('/exam/table', 'add')
                "
                class="el-button float-right el-button--default el-button--primary search_btn_add"
                :to="'/question_view/view?exam_id=' + query.exam_id+'&subject_name='+this.$route.query.subject_name"
                ><span>添加</span>
              </router-link> -->
              <el-button  v-if="user_group == '管理员' || $check_action('/exam/table', 'add')" class="float-right  search_btn_add" @click="$router.push('/question_view/view?exam_id=' + query.exam_id+'&subject_name='+this.$route.query.subject_name)">添加</el-button>
					
          </el-col>
          
        </el-col>
      </el-row>
    </el-form>
    <el-table
      border
      :data="list"
      @selection-change="selectionChange"
      @sort-change="$sortChange"
      style="width: 100%"
      stripe
    >
      <el-table-column fixed type="selection" tooltip-effect="dark" width="50">
      </el-table-column>

      <el-table-column fixed prop="subject_name" label="科目" min-width="120">
      </el-table-column>

      <el-table-column fixed prop="type" label="类型" min-width="120">
      </el-table-column>

      <el-table-column prop="title" label="题目" min-width="200">
      </el-table-column>

      <el-table-column prop="score" label="分值" min-width="180">
      </el-table-column>

      <el-table-column prop="question_order" label="排序" min-width="180">
      </el-table-column>

      <el-table-column
        sortable
        prop="create_time"
        label="创建时间"
        min-width="200"
      >
        <template slot-scope="scope">
          {{ $toTime(scope.row["create_time"], "yyyy-MM-dd hh:mm:ss") }}
        </template>
      </el-table-column>

      <el-table-column
        sortable
        prop="update_time"
        label="更新时间"
        min-width="200"
      >
        <template slot-scope="scope">
          {{ $toTime(scope.row["update_time"], "yyyy-MM-dd hh:mm:ss") }}
        </template>
      </el-table-column>

      <!-- 操作 -->
      <el-table-column fixed="right" label="操作" width="150">
        <template slot-scope="scope">
          <div class="view_a">
          <router-link
            class="e-button el-button--small is-plain el-button--primary"
            v-if="user_group == '管理员' || $check_action('/exam/table', 'set')"
            :to="'/exam_subject/question_view?' + field + '=' + scope.row[field]"
            size="small"
          >
            <span>详情</span>
          </router-link>
          </div>
        </template>
      </el-table-column>
      <!-- /操作 -->
    </el-table>

    <!-- 分页器 -->
    <div class="mt text_center">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="query.page"
        :page-sizes="[7, 10, 30, 100]"
        :page-size="query.size"
        layout="total, sizes, prev, pager, next, jumper"
        :total="count"
      >
      </el-pagination>
    </div>
    <!-- /分页器 -->
  </el-main>
</template>

<script>
import mixin from "@/mixins/page.js";

export default {
  mixins: [mixin],
  data() {
    return {
      // 获取数据地址
      url_get_list: "~/api/subject_exam_question/get_list?like=0",
      url_del: "~/api/subject_exam_question/del?",

      // 字段ID
      field: "exam_question_id",

      // 查询
      query: {
        size: 10,
        page: 1,
        exam_id: 0,
        type: "",
        title: "",
        orderby: "question_order",
      },

      // 数据
      list: [],
    };
  },
  methods: {
    deleteRow(index, rows) {
      rows.splice(index, 1);
    },
    /**
     * 重置
     */
    reset() {
      let exam_id = { exam_id: this.query.exam_id };
      let orderby = { exam_id: this.query.orderby };
      $.clear(this.query);
      $.push(this.query, this.config);
      $.push(this.query, exam_id);
      $.push(this.query, orderby);
      $.push(this.query, {subject_name:this.$route.query.subject_name});
      this.get_list();
    },
  },
  created() {},
};
</script>

<style type="text/css">
</style>
