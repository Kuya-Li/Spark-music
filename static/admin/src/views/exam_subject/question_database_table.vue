<template>
  <el-main class="bg table_wrap">
    <el-form
      label-position="right"
      :model="query"
      class="form p_4"
      label-width="120"
    >
      <el-row class="rows row1">
        <el-col :xs="24" :sm="24" :lg="8" class="el_form_search_wrap">
          <el-form-item label="科目名称">
            <el-select v-model="query.subject_name">
              <el-option
                v-for="obj in list_subject"
                :key="obj.name"
                :label="obj.name"
                :value="obj.name"
              >
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>

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
          <el-col :xs="24" :sm="12" :lg="12" class="search_btn_1">
           
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
                  user_group == '管理员' ||
                  $check_action('/exam_question_database/table', 'del')
                "
                class="float-right search_btn_del"
                type="danger"
                @click="delInfo()"
                >删除</el-button
              >
              <!-- <router-link
                v-if="
                  user_group == '管理员' ||
                  $check_action('/exam_question_database/table', 'add')
                "
                class="el-button float-right el-button--default el-button--primary search_btn_add"
                :to="'/exam_subject/question_database_view'"
                ><span>添加</span>
              </router-link> -->
              <el-button  v-if="user_group == '管理员' || $check_action('/exam_question_database/table', 'add')" class="float-right  search_btn_add" @click="$router.push('/exam_subject/question_database_view')">添加</el-button>
					
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
          <router-link
            class="e-button el-button--small is-plain el-button--primary"
            v-if="
              user_group == '管理员' ||
              $check_action('/exam_question_database/table', 'set')
            "
            :to="
              '/exam_subject/question_database_view?' + field + '=' + scope.row[field]
            "
            size="small"
          >
            <span>详情</span>
          </router-link>
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
      url_get_list: "~/api/exam_question_database/get_list?like=0",
      url_del: "~/api/exam_question_database/del?",

      // 字段ID
      field: "exam_question_id",

      // 查询
      query: {
        size: 10,
        page: 1,
        type: "",
        title: "",
        subject_name:"",
        orderby: "create_time desc",
      },

      // 数据
      list: [],

      list_subject: [],
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
      $.clear(this.query);
      $.push(this.query, this.config);
      this.get_list();
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
  },
  created() {
    this.get_subject_list();
  },
};
</script>

<style type="text/css">
</style>
