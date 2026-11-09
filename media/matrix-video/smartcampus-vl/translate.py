#!/usr/bin/env python3
"""Translate the SmartCampus copy of the Huzhou dashboard example into English.
Only string literal values and comments are changed; identifiers stay as they are."""
import re, sys, glob, os, json

ROOT = sys.argv[1]
CJK = re.compile('[　-鿿＀-￯]')

S = {
    # header / platform meta
    "湖州学院": "Lakeview University",
    "党建管理与服务平台": "Smart Campus Operations Dashboard",
    "湖大": "LU",
    # left column: campus population
    "党员情况": "Campus Population",
    "党组织数": "Schools",
    "党支部数": "Student Clubs",
    "组织员数": "Research Centers",
    "在线学生党员": "Students",
    "在岗职工党员": "Faculty & Staff",
    "其他": "Contractors",
    "流入党员": "Visitors",
    "机械工程学院": "Student Attendance",
    "教师党员比例": "Staff On Duty",
    # campus sites map
    "校企地共同体": "Campus Sites",
    "嘉兴": "North Campus",
    "杭州市西湖区": "Main Campus",
    "湖州": "East Campus",
    "绍兴": "Science Park",
    "宁波": "Medical Center",
    "中国 · 浙江": "5 sites · 1 network",
    "湖州 · 浙北": "Main Campus",
    "长三角共建覆盖区域示意": "Overview of campus and partner sites",
    # key projects
    "培育创建项目": "Key Projects",
    "省级": "State",
    "校级": "Campus",
    "科艺学院与设计学院叫工党支部": "Library Smart Seating Upgrade",
    "校级样板支部": "Green Building Pilot",
    "双带头人教师党支部书记工作室": "Faculty Mentorship Studio",
    "党建研究培育课题": "Student Wellbeing Research Grant",
    # workforce tabs
    "中层干部": "Faculty",
    "科级干部": "Staff",
    "双强双高": "Researchers",
    "干部统计（中层 / 科级 / 双强双高）": "Workforce Overview",
    "性别之比": "Gender Ratio",
    "男": "Male",
    "女": "Female",
    "年龄分布": "Age Distribution",
    "35及以下": "35 & under",
    "56以上": "56 & over",
    "职称分布": "Seniority",
    "正高": "Senior",
    "副高": "Associate",
    "中级": "Mid-level",
    "初级": "Junior",
    # bottom row
    "组织管理": "Help Desk",
    "任务发布数": "Opened",
    "任务提交数": "Resolved",
    "党费缴纳": "Occupancy",
    "党费缴纳 (%)": "Occupancy (%)",
    "1月": "Jan", "2月": "Feb", "3月": "Mar", "4月": "Apr", "5月": "May",
    "干部兼职情况": "Campus Events",
    "社会团体兼职A": "Lectures",
    "社会团体兼职B": "Sports",
    "社会团体兼职C": "Arts & Culture",
    "社会团体兼职D": "Other",
    # middle column
    "学习宣传": "Engagement & Communications",
    "媒体传真": "Media Coverage Index",
    "继续教育学院": "Continuing Education",
    "体育教研部": "Athletics Department",
    "国际教育学院、国际时装技术学院": "International Programs",
    "马克思主义学院": "School of Humanities",
    "启新学院、创业学院": "Innovation & Entrepreneurship",
    "外国语学院": "School of Languages",
    "法政学院、史量才新闻与传播学院": "Law, Policy & Journalism",
    "*各单位综合分值根据在学校新闻网、公众号、校服、新媒体号以及校外媒体发布条数测算所得（截止 2022 年 8 月 24 日）":
        "*Composite score per unit, based on items published on the university news site, official social accounts, campus media and external outlets (as of Aug 24, 2022)",
    "融媒体动态": "Social Media Reach",
    "2022 年度学校官方平台": "Official channels, 2022",
    "微信公众号": "Instagram",
    "微博": "LinkedIn",
    "视频号": "YouTube",
    "抖音": "TikTok",
    "136.5万": "1.37M",
    "5600万": "56M",
    "232万": "2.32M",
    "110万": "1.1M",
    "6万": "60K",
    "发布数(条)": "Posts",
    "总阅读量(次)": "Total views",
    "发布": "Posts",
    "阅读": "Views",
    "理论学习": "Training & Workshops",
    "已发布学习任务": "Courses published",
    "5 条": "5",
    "各单位共计学习": "Sessions held",
    "各单位共计": "Sessions held",
    "102 次": "102",
    "年度": "Year",
    "月度": "Month",
    "材料学院": "Materials",
    "服装学院": "Design",
    "计算机学院": "Computing",
    "机械学院": "Engineering",
    "信息学院": "Info Science",
    "经管学院": "Business",
    "舆情观察": "Satisfaction Survey",
    "党委委员": "Students",
    "纪委委员": "Staff",
    "40及以下": "Dining",
    "41-50": "Housing",
    "51-60": "Library",
    "60及以下": "IT Services",
    # right column
    "纪检监察": "Facilities & Safety",
    "国有房产大数据监督": "Building Energy Monitoring",
    "科研安": "Lab Safety",
    "预警模型": "Alert rules",
    "预警排行 TOP10": "Top 10 alerts",
    "预警 TOP10": "Top 10 alerts",
    "蓝色预警": "Low",
    "黄色预警": "Medium",
    "红色预警": "High",
    "蓝": "Low",
    "黄": "Med",
    "红": "High",
    **{f"模型{i}": f"Zone {i}" for i in range(1, 11)},
    "重大事项跟进监督": "Maintenance Work Orders",
    "整改措施(项)": "Work orders (total)",
    "已完成": "Completed",
    # code-level strings
    "加载失败: ": "Failed to load: ",
    # @meta descriptions
    "重新加载大屏全部数据": "Reload all dashboard data",
    "是否成功": "Whether the call succeeded",
    "读取党建大屏全部数据切片（read-only，无任何 write 操作）": "Read every data slice of the campus dashboard (read-only, no write operations)",
    "错误信息": "Error message",
    "党员情况 3 个 KPI": "Campus population: 3 KPIs",
    "党员环图 4 切片": "Population donut: 4 slices",
    "右侧两条进度": "Two attendance progress bars",
    "培育创建项目列表": "Key project list",
    "干部 tab 元数据": "Workforce tab metadata",
    "干部性别": "Workforce gender ratio",
    "干部年龄": "Workforce age distribution",
    "干部职称": "Workforce seniority",
    "组织管理 KPI": "Help desk KPIs",
    "干部兼职": "Campus events",
    "预警汇总": "Alert summaries",
    "预警柱状图": "Alert bar chart",
    "重大事项": "Maintenance work orders",
    "平台 meta": "Platform meta",
    # VL-FIXED-LIST-OK reasons
    "2 KPI 固定": "2 fixed KPIs",
    "2 组预警块固定": "2 fixed alert groups",
    "2 院进度固定": "2 fixed progress bars",
    "2 预警组固定": "2 fixed alert groups",
    "3 个 tab chip 固定": "3 fixed tab chips",
    "4 兼职 legend": "4 event legend items",
    "4 兼职固定": "4 fixed event slices",
    "4 切片 legend 固定": "4 fixed slice legend items",
    "4 年龄段舆情": "4 survey areas",
    "4 年龄段舆情固定": "4 fixed survey areas",
    "5 列发布数": "5 post-count columns",
    "5 列表头": "5 header columns",
    "5 列阅读量": "5 view-count columns",
    "5 月柱图固定": "5 fixed monthly bars",
    "6 学院双柱": "6 department paired bars",
    "6 学院双柱图固定": "6 fixed department paired bars",
    "Top10 预警柱图": "Top 10 alert bars",
    "Top10 预警柱图固定": "Top 10 fixed alert bars",
    "固定 2 条 college ratio": "2 fixed attendance ratios",
    "固定 3 行 KPI": "3 fixed KPI rows",
    "固定 3 项 KPI": "3 fixed KPIs",
    "固定 5 条项目": "5 fixed projects",
    "固定 5 项目": "5 fixed projects",
    "媒体排行 7 固定": "7 fixed media ranks",
    "年龄段 4 条固定": "4 fixed age bands",
    "年龄段固定": "fixed age bands",
    "性别 legend 2 条固定": "2 fixed gender legend items",
    "性别 legend 固定": "fixed gender legend",
    "环图 4 个 legend 固定": "4 fixed donut legend items",
    "职称 legend 4 条固定": "4 fixed seniority legend items",
    "职称 legend 固定": "fixed seniority legend",
    "融媒体平台 5 行固定": "5 fixed social platforms",
}
# non-Chinese strings that must change with the re-theme
S_EXTRA = {
    "HUZHOU UNIVERSITY": "SMART CAMPUS · OPERATIONS CENTER",
}

# whole-comment translations (text after "//", stripped), applied after string pass
C = {
    "===== 驾驶舱响应式：所有纵向尺寸/字号用 vh，宽度用 %，16:9 各视口（1920/1600/1366/1280）等比一屏闭合 =====":
        "===== Responsive cockpit: vertical sizes/fonts in vh, widths in %, every 16:9 viewport (1920/1600/1366/1280) fits on one screen =====",
    "========== Module 10: 学习宣传 ==========": "========== Module 10: Engagement & Communications ==========",
    "========== Module 11-13: 纪检监察 ==========": "========== Module 11-13: Facilities & Safety ==========",
    "========== Module 14: 重大事项跟进监督 ==========": "========== Module 14: Maintenance Work Orders ==========",
    "========== Module 1: 党员情况 ==========": "========== Module 1: Campus Population ==========",
    "========== Module 2: 校企地共同体 ==========": "========== Module 2: Campus Sites ==========",
    "========== Module 3: 培育创建项目 ==========": "========== Module 3: Key Projects ==========",
    "========== Module 4-6: 干部 Tab ==========": "========== Module 4-6: Workforce Tabs ==========",
    "========== Module 7: 组织管理 KPI ==========": "========== Module 7: Help Desk KPIs ==========",
    "========== Module 8: 党费缴纳柱状图 ==========": "========== Module 8: Occupancy Bar Chart ==========",
    "========== Module 9: 干部兼职情况 ==========": "========== Module 9: Campus Events ==========",
    "============ MIDDLE COLUMN (50%) — 学习宣传 ============": "============ MIDDLE COLUMN (50%) — Engagement & Communications ============",
    "============ RIGHT COLUMN (25%) — 纪检监察 ============": "============ RIGHT COLUMN (25%) — Facilities & Safety ============",
    "— 党员情况 (flex 21) —": "— Campus Population (flex 21) —",
    "— 干部 Tab (flex 24) —": "— Workforce Tabs (flex 24) —",
    "— 年龄分布（独立横条列表）": "— Age distribution (standalone horizontal bar list)",
    "— 底部 3 列 (flex 18) —": "— Bottom 3 columns (flex 18) —",
    "— 性别 + 职称（一行两个圆环）": "— Gender + seniority (two donuts in one row)",
    "— 校企地共同体 + 培育创建项目 (flex 21) —": "— Campus Sites + Key Projects (flex 21) —",
    "一次性加载大屏全部 19 个数据切片（纯展示，无写入）": "Load all 19 dashboard data slices at once (display only, no writes)",
    "党员情况 KPI 三件套": "Campus population: 3 KPIs",
    "党员情况右侧两条横向进度": "Campus population: two horizontal progress bars on the right",
    "党员情况环图 4 切片": "Campus population donut: 4 slices",
    "党费缴纳 1-5月": "Occupancy, Jan-May",
    "唯一首页 — 党建大屏；根据 viewport 切换 PC 三列 vs Mobile 单列": "Single home page: Smart Campus dashboard; switches between PC three-column and mobile single-column by viewport",
    "国有房产 / 科研安 两块": "Building Energy / Lab Safety blocks",
    "培育创建项目 5 条": "Key projects: 5 rows",
    "媒体传真": "Media coverage index",
    "媒体传真排行": "Media coverage ranking",
    "干部 Tab 元数据": "Workforce tab metadata",
    "干部兼职情况环图": "Campus events donut",
    "干部年龄分布 — 每个 tab 各 4 条": "Workforce age distribution: 4 rows per tab",
    "干部性别之比 — 每个 tab 各 2 条": "Workforce gender ratio: 2 rows per tab",
    "干部职称分布 — 每个 tab 各 4 条": "Workforce seniority: 4 rows per tab",
    "平台 Meta — 学校名+标题+顶部环图中心总数": "Platform meta: university name + title + events donut center total",
    "年龄分布": "Age distribution",
    "性别之比": "Gender ratio",
    "理论学习": "Training & workshops",
    "理论学习双系列柱状图": "Training & workshops: two-series bar chart",
    "窄列响应式：环图在上、图例全宽在下，避免 1280 窄列时图例文字换行": "Narrow-column layout: donut on top, full-width legend below, so legend text does not wrap at 1280",
    "纪检监察预警 Top10 柱状图": "Facilities & safety alerts: top 10 bar chart",
    "纪检监察预警汇总": "Facilities & safety alert summaries",
    "组织管理 KPI": "Help desk KPIs",
    "职称分布": "Seniority",
    "舆情观察": "Satisfaction survey",
    "舆情观察面积图": "Satisfaction survey chart",
    "融媒体动态": "Social media reach",
    "融媒体动态 — 数据卡片化": "Social media reach: card layout",
    "融媒体动态表": "Social media reach table",
    "重大事项跟进监督": "Maintenance work orders",
}

STR_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')
stats = {}
missing = []
for f in sorted(glob.glob(os.path.join(ROOT, '**/*.*'), recursive=True)):
    if '/.vl-code/' in f or '/Process/' in f or f.endswith('VL.md'):
        continue
    src = open(f, encoding='utf-8').read()
    nstr = 0; ncom = 0
    def sub_str(m):
        global nstr
        s = m.group(1)
        if s in S:
            return '"' + S[s] + '"'
        if s in S_EXTRA:
            return '"' + S_EXTRA[s] + '"'
        if CJK.search(s):
            missing.append((f, s))
        return m.group(0)
    out_lines = []
    for line in src.split('\n'):
        new = STR_RE.sub(sub_str, line)
        nstr += len([1 for a, b in zip(STR_RE.findall(line), STR_RE.findall(new)) if a != b])
        idx = new.find('//')
        # only treat as comment if the // is outside a string literal
        if idx >= 0:
            before = new[:idx]
            if before.count('"') % 2 == 0:
                body = new[idx + 2:]
                key = body.strip()
                if CJK.search(key):
                    if key in C:
                        lead = body[:len(body) - len(body.lstrip())]
                        new = new[:idx + 2] + lead + C[key]
                        ncom += 1
                    else:
                        missing.append((f, 'COMMENT: ' + key))
        out_lines.append(new)
    out = '\n'.join(out_lines)
    if out != src:
        open(f, 'w', encoding='utf-8').write(out)
    rel = os.path.relpath(f, ROOT)
    left = [l for l in out.split('\n') if CJK.search(l)]
    stats[rel] = {'string_literals_changed': nstr, 'comments_translated': ncom, 'lines_with_cjk_left': len(left)}

print(json.dumps(stats, indent=1, ensure_ascii=False))
for f, s in missing:
    print('MISSING', os.path.relpath(f, ROOT), s)
