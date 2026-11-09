// VL_VERSION:4.3.0
<ServiceDomain-Dashboard>

# Backend Tree
<VirtualTable-VTOrgStats "vtOrgStats"> sourceTable:OrgStats
-<Field-label> type:STRING
-<Field-value> type:INT
-<Field-sortOrder> type:INT

<VirtualTable-VTPartyMemberSlices "vtPartyMember"> sourceTable:PartyMemberSlices
-<Field-label> type:STRING
-<Field-value> type:INT
-<Field-color> type:STRING
-<Field-showLegend> type:INT
-<Field-sortOrder> type:INT

<VirtualTable-VTCollegeRatios "vtCollegeRatios"> sourceTable:CollegeRatios
-<Field-label> type:STRING
-<Field-currentVal> type:INT
-<Field-totalVal> type:INT
-<Field-pctLabel> type:STRING
-<Field-pctNum> type:INT
-<Field-color> type:STRING
-<Field-sortOrder> type:INT

<VirtualTable-VTIncubationProjects "vtIncubation"> sourceTable:IncubationProjects
-<Field-title> type:STRING
-<Field-level> type:STRING
-<Field-sortOrder> type:INT

<VirtualTable-VTCadreTabs "vtCadreTabs"> sourceTable:CadreTabs
-<Field-tabKey> type:STRING
-<Field-label> type:STRING
-<Field-sortOrder> type:INT

<VirtualTable-VTCadreGenders "vtCadreGenders"> sourceTable:CadreGenders
-<Field-tabKey> type:STRING
-<Field-label> type:STRING
-<Field-value> type:INT
-<Field-color> type:STRING
-<Field-sortOrder> type:INT

<VirtualTable-VTCadreAges "vtCadreAges"> sourceTable:CadreAges
-<Field-tabKey> type:STRING
-<Field-label> type:STRING
-<Field-value> type:INT
-<Field-pctNum> type:INT
-<Field-color> type:STRING
-<Field-sortOrder> type:INT

<VirtualTable-VTCadreTitles "vtCadreTitles"> sourceTable:CadreTitles
-<Field-tabKey> type:STRING
-<Field-label> type:STRING
-<Field-value> type:INT
-<Field-color> type:STRING
-<Field-sortOrder> type:INT

<VirtualTable-VTOrgKpis "vtOrgKpis"> sourceTable:OrgKpis
-<Field-label> type:STRING
-<Field-value> type:INT
-<Field-color> type:STRING
-<Field-sortOrder> type:INT

<VirtualTable-VTDuesBars "vtDuesBars"> sourceTable:DuesBars
-<Field-monthLabel> type:STRING
-<Field-value> type:INT
-<Field-sortOrder> type:INT

<VirtualTable-VTSideJobSlices "vtSideJob"> sourceTable:SideJobSlices
-<Field-label> type:STRING
-<Field-value> type:INT
-<Field-percent> type:STRING
-<Field-color> type:STRING
-<Field-sortOrder> type:INT

<VirtualTable-VTMediaRanks "vtMediaRanks"> sourceTable:MediaRanks
-<Field-label> type:STRING
-<Field-value> type:STRING
-<Field-barPct> type:INT
-<Field-sortOrder> type:INT

<VirtualTable-VTMediaTable "vtMediaTable"> sourceTable:MediaTable
-<Field-platform> type:STRING
-<Field-postCount> type:STRING
-<Field-readCount> type:STRING
-<Field-sortOrder> type:INT

<VirtualTable-VTStudyBars "vtStudyBars"> sourceTable:StudyBars
-<Field-label> type:STRING
-<Field-annualVal> type:INT
-<Field-monthlyVal> type:INT
-<Field-sortOrder> type:INT

<VirtualTable-VTOpinionAreas "vtOpinionAreas"> sourceTable:OpinionAreas
-<Field-ageLabel> type:STRING
-<Field-partyVal> type:INT
-<Field-disciplineVal> type:INT
-<Field-sortOrder> type:INT

<VirtualTable-VTWarningSummaries "vtWarningSummaries"> sourceTable:WarningSummaries
-<Field-groupKey> type:STRING
-<Field-title> type:STRING
-<Field-modelCount> type:INT
-<Field-blueCount> type:INT
-<Field-yellowCount> type:INT
-<Field-redCount> type:INT
-<Field-sortOrder> type:INT

<VirtualTable-VTWarningBars "vtWarningBars"> sourceTable:WarningBars
-<Field-groupKey> type:STRING
-<Field-modelLabel> type:STRING
-<Field-value> type:INT
-<Field-color> type:STRING
-<Field-sortOrder> type:INT

<VirtualTable-VTMajorEvents "vtMajorEvents"> sourceTable:MajorEvents
-<Field-totalCount> type:INT
-<Field-doneCount> type:INT
-<Field-pctLabel> type:STRING
-<Field-pctNum> type:INT

<VirtualTable-VTPlatformMeta "vtPlatformMeta"> sourceTable:PlatformMeta
-<Field-schoolCn> type:STRING
-<Field-schoolEn> type:STRING
-<Field-title> type:STRING
-<Field-sideJobTotal> type:INT

# Services
// Load all 19 dashboard data slices at once (display only, no writes)
// @meta service description:"Read every data slice of the campus dashboard (read-only, no write operations)" returns:({success:{description:"Whether the call succeeded"},message:{description:"Error message"},orgStats:{description:"Campus population: 3 KPIs"},memberDonut:{description:"Population donut: 4 slices"},collegeRatios:{description:"Two attendance progress bars"},incubationProjects:{description:"Key project list"},cadreTabs:{description:"Workforce tab metadata"},cadreGenders:{description:"Workforce gender ratio"},cadreAges:{description:"Workforce age distribution"},cadreTitles:{description:"Workforce seniority"},orgKpis:{description:"Help desk KPIs"},duesBars:{description:"Occupancy"},sideJobSlices:{description:"Campus events"},mediaRanks:{description:"Media Coverage Index"},mediaTable:{description:"Social Media Reach"},studyBars:{description:"Training & Workshops"},opinionAreas:{description:"Satisfaction Survey"},warningSummaries:{description:"Alert summaries"},warningBars:{description:"Alert bar chart"},majorEvent:{description:"Maintenance work orders"},platformMeta:{description:"Platform meta"}})
PUBLIC_SERVICE GetDashboardData();RETURN {success:BOOL,message:STRING,orgStats:[{label:STRING,value:INT,sortOrder:INT}],memberDonut:[{label:STRING,value:INT,color:STRING,showLegend:INT,sortOrder:INT}],collegeRatios:[{label:STRING,currentVal:INT,totalVal:INT,pctLabel:STRING,pctNum:INT,color:STRING,sortOrder:INT}],incubationProjects:[{title:STRING,level:STRING,sortOrder:INT}],cadreTabs:[{tabKey:STRING,label:STRING,sortOrder:INT}],cadreGenders:[{tabKey:STRING,label:STRING,value:INT,color:STRING,sortOrder:INT}],cadreAges:[{tabKey:STRING,label:STRING,value:INT,pctNum:INT,color:STRING,sortOrder:INT}],cadreTitles:[{tabKey:STRING,label:STRING,value:INT,color:STRING,sortOrder:INT}],orgKpis:[{label:STRING,value:INT,color:STRING,sortOrder:INT}],duesBars:[{monthLabel:STRING,value:INT,sortOrder:INT}],sideJobSlices:[{label:STRING,value:INT,percent:STRING,color:STRING,sortOrder:INT}],mediaRanks:[{label:STRING,value:STRING,barPct:INT,sortOrder:INT}],mediaTable:[{platform:STRING,postCount:STRING,readCount:STRING,sortOrder:INT}],studyBars:[{label:STRING,annualVal:INT,monthlyVal:INT,sortOrder:INT}],opinionAreas:[{ageLabel:STRING,partyVal:INT,disciplineVal:INT,sortOrder:INT}],warningSummaries:[{groupKey:STRING,title:STRING,modelCount:INT,blueCount:INT,yellowCount:INT,redCount:INT,sortOrder:INT}],warningBars:[{groupKey:STRING,modelLabel:STRING,value:INT,color:STRING,sortOrder:INT}],majorEvent:{totalCount:INT,doneCount:INT,pctLabel:STRING,pctNum:INT},platformMeta:{schoolCn:STRING,schoolEn:STRING,title:STRING,sideJobTotal:INT}};EXPOSE {method:"POST",receive:"JSON",response:"JSON"}
-ensureDemoData() -> _seed
-IF !_seed.success
--RETURN {success:false,message:"demo data initialization failed",orgStats:[],memberDonut:[],collegeRatios:[],incubationProjects:[],cadreTabs:[],cadreGenders:[],cadreAges:[],cadreTitles:[],orgKpis:[],duesBars:[],sideJobSlices:[],mediaRanks:[],mediaTable:[],studyBars:[],opinionAreas:[],warningSummaries:[],warningBars:[],majorEvent:{totalCount:0,doneCount:0,pctLabel:"",pctNum:0},platformMeta:{schoolCn:"",schoolEn:"",title:"",sideJobTotal:0}}
-<VirtualTable-VTOrgStats "vtOrgStats">.select(null,[["sortOrder","asc"]],[0,100],["label","value","sortOrder"],null) -> _orgStatsResult
-IF !_orgStatsResult.success
--RETURN {success:false,message:"orgStats load failed",orgStats:[],memberDonut:[],collegeRatios:[],incubationProjects:[],cadreTabs:[],cadreGenders:[],cadreAges:[],cadreTitles:[],orgKpis:[],duesBars:[],sideJobSlices:[],mediaRanks:[],mediaTable:[],studyBars:[],opinionAreas:[],warningSummaries:[],warningBars:[],majorEvent:{totalCount:0,doneCount:0,pctLabel:"",pctNum:0},platformMeta:{schoolCn:"",schoolEn:"",title:"",sideJobTotal:0}}
-_orgStats([{label:STRING,value:INT,sortOrder:INT}]) = []
-FOR (_r,_i) IN _orgStatsResult.dataArray
--_orgStats.push({label:_r.label,value:_r.value,sortOrder:_r.sortOrder})

-<VirtualTable-VTPartyMemberSlices "vtPartyMember">.select(null,[["sortOrder","asc"]],[0,100],["label","value","color","showLegend","sortOrder"],null) -> _memberResult
-IF !_memberResult.success
--RETURN {success:false,message:"memberDonut load failed",orgStats:_orgStats,memberDonut:[],collegeRatios:[],incubationProjects:[],cadreTabs:[],cadreGenders:[],cadreAges:[],cadreTitles:[],orgKpis:[],duesBars:[],sideJobSlices:[],mediaRanks:[],mediaTable:[],studyBars:[],opinionAreas:[],warningSummaries:[],warningBars:[],majorEvent:{totalCount:0,doneCount:0,pctLabel:"",pctNum:0},platformMeta:{schoolCn:"",schoolEn:"",title:"",sideJobTotal:0}}
-_memberDonut([{label:STRING,value:INT,color:STRING,showLegend:INT,sortOrder:INT}]) = []
-FOR (_r,_i) IN _memberResult.dataArray
--_memberDonut.push({label:_r.label,value:_r.value,color:_r.color,showLegend:_r.showLegend,sortOrder:_r.sortOrder})

-<VirtualTable-VTCollegeRatios "vtCollegeRatios">.select(null,[["sortOrder","asc"]],[0,100],["label","currentVal","totalVal","pctLabel","pctNum","color","sortOrder"],null) -> _collegeResult
-_collegeRatios([{label:STRING,currentVal:INT,totalVal:INT,pctLabel:STRING,pctNum:INT,color:STRING,sortOrder:INT}]) = []
-IF _collegeResult.success
--FOR (_r,_i) IN _collegeResult.dataArray
---_collegeRatios.push({label:_r.label,currentVal:_r.currentVal,totalVal:_r.totalVal,pctLabel:_r.pctLabel,pctNum:_r.pctNum,color:_r.color,sortOrder:_r.sortOrder})

-<VirtualTable-VTIncubationProjects "vtIncubation">.select(null,[["sortOrder","asc"]],[0,100],["title","level","sortOrder"],null) -> _incubResult
-_incubationProjects([{title:STRING,level:STRING,sortOrder:INT}]) = []
-IF _incubResult.success
--FOR (_r,_i) IN _incubResult.dataArray
---_incubationProjects.push({title:_r.title,level:_r.level,sortOrder:_r.sortOrder})

-<VirtualTable-VTCadreTabs "vtCadreTabs">.select(null,[["sortOrder","asc"]],[0,100],["tabKey","label","sortOrder"],null) -> _cadreTabsResult
-_cadreTabs([{tabKey:STRING,label:STRING,sortOrder:INT}]) = []
-IF _cadreTabsResult.success
--FOR (_r,_i) IN _cadreTabsResult.dataArray
---_cadreTabs.push({tabKey:_r.tabKey,label:_r.label,sortOrder:_r.sortOrder})

-<VirtualTable-VTCadreGenders "vtCadreGenders">.select(null,[["sortOrder","asc"]],[0,500],["tabKey","label","value","color","sortOrder"],null) -> _cadreGendersResult
-_cadreGenders([{tabKey:STRING,label:STRING,value:INT,color:STRING,sortOrder:INT}]) = []
-IF _cadreGendersResult.success
--FOR (_r,_i) IN _cadreGendersResult.dataArray
---_cadreGenders.push({tabKey:_r.tabKey,label:_r.label,value:_r.value,color:_r.color,sortOrder:_r.sortOrder})

-<VirtualTable-VTCadreAges "vtCadreAges">.select(null,[["sortOrder","asc"]],[0,500],["tabKey","label","value","pctNum","color","sortOrder"],null) -> _cadreAgesResult
-_cadreAges([{tabKey:STRING,label:STRING,value:INT,pctNum:INT,color:STRING,sortOrder:INT}]) = []
-IF _cadreAgesResult.success
--FOR (_r,_i) IN _cadreAgesResult.dataArray
---_cadreAges.push({tabKey:_r.tabKey,label:_r.label,value:_r.value,pctNum:_r.pctNum,color:_r.color,sortOrder:_r.sortOrder})

-<VirtualTable-VTCadreTitles "vtCadreTitles">.select(null,[["sortOrder","asc"]],[0,500],["tabKey","label","value","color","sortOrder"],null) -> _cadreTitlesResult
-_cadreTitles([{tabKey:STRING,label:STRING,value:INT,color:STRING,sortOrder:INT}]) = []
-IF _cadreTitlesResult.success
--FOR (_r,_i) IN _cadreTitlesResult.dataArray
---_cadreTitles.push({tabKey:_r.tabKey,label:_r.label,value:_r.value,color:_r.color,sortOrder:_r.sortOrder})

-<VirtualTable-VTOrgKpis "vtOrgKpis">.select(null,[["sortOrder","asc"]],[0,100],["label","value","color","sortOrder"],null) -> _orgKpisResult
-_orgKpis([{label:STRING,value:INT,color:STRING,sortOrder:INT}]) = []
-IF _orgKpisResult.success
--FOR (_r,_i) IN _orgKpisResult.dataArray
---_orgKpis.push({label:_r.label,value:_r.value,color:_r.color,sortOrder:_r.sortOrder})

-<VirtualTable-VTDuesBars "vtDuesBars">.select(null,[["sortOrder","asc"]],[0,100],["monthLabel","value","sortOrder"],null) -> _duesBarsResult
-_duesBars([{monthLabel:STRING,value:INT,sortOrder:INT}]) = []
-IF _duesBarsResult.success
--FOR (_r,_i) IN _duesBarsResult.dataArray
---_duesBars.push({monthLabel:_r.monthLabel,value:_r.value,sortOrder:_r.sortOrder})

-<VirtualTable-VTSideJobSlices "vtSideJob">.select(null,[["sortOrder","asc"]],[0,100],["label","value","percent","color","sortOrder"],null) -> _sideJobResult
-_sideJobSlices([{label:STRING,value:INT,percent:STRING,color:STRING,sortOrder:INT}]) = []
-IF _sideJobResult.success
--FOR (_r,_i) IN _sideJobResult.dataArray
---_sideJobSlices.push({label:_r.label,value:_r.value,percent:_r.percent,color:_r.color,sortOrder:_r.sortOrder})

-<VirtualTable-VTMediaRanks "vtMediaRanks">.select(null,[["sortOrder","asc"]],[0,100],["label","value","barPct","sortOrder"],null) -> _mediaRanksResult
-_mediaRanks([{label:STRING,value:STRING,barPct:INT,sortOrder:INT}]) = []
-IF _mediaRanksResult.success
--FOR (_r,_i) IN _mediaRanksResult.dataArray
---_mediaRanks.push({label:_r.label,value:_r.value,barPct:_r.barPct,sortOrder:_r.sortOrder})

-<VirtualTable-VTMediaTable "vtMediaTable">.select(null,[["sortOrder","asc"]],[0,100],["platform","postCount","readCount","sortOrder"],null) -> _mediaTableResult
-_mediaTable([{platform:STRING,postCount:STRING,readCount:STRING,sortOrder:INT}]) = []
-IF _mediaTableResult.success
--FOR (_r,_i) IN _mediaTableResult.dataArray
---_mediaTable.push({platform:_r.platform,postCount:_r.postCount,readCount:_r.readCount,sortOrder:_r.sortOrder})

-<VirtualTable-VTStudyBars "vtStudyBars">.select(null,[["sortOrder","asc"]],[0,100],["label","annualVal","monthlyVal","sortOrder"],null) -> _studyBarsResult
-_studyBars([{label:STRING,annualVal:INT,monthlyVal:INT,sortOrder:INT}]) = []
-IF _studyBarsResult.success
--FOR (_r,_i) IN _studyBarsResult.dataArray
---_studyBars.push({label:_r.label,annualVal:_r.annualVal,monthlyVal:_r.monthlyVal,sortOrder:_r.sortOrder})

-<VirtualTable-VTOpinionAreas "vtOpinionAreas">.select(null,[["sortOrder","asc"]],[0,100],["ageLabel","partyVal","disciplineVal","sortOrder"],null) -> _opinionResult
-_opinionAreas([{ageLabel:STRING,partyVal:INT,disciplineVal:INT,sortOrder:INT}]) = []
-IF _opinionResult.success
--FOR (_r,_i) IN _opinionResult.dataArray
---_opinionAreas.push({ageLabel:_r.ageLabel,partyVal:_r.partyVal,disciplineVal:_r.disciplineVal,sortOrder:_r.sortOrder})

-<VirtualTable-VTWarningSummaries "vtWarningSummaries">.select(null,[["sortOrder","asc"]],[0,100],["groupKey","title","modelCount","blueCount","yellowCount","redCount","sortOrder"],null) -> _wSumResult
-_warningSummaries([{groupKey:STRING,title:STRING,modelCount:INT,blueCount:INT,yellowCount:INT,redCount:INT,sortOrder:INT}]) = []
-IF _wSumResult.success
--FOR (_r,_i) IN _wSumResult.dataArray
---_warningSummaries.push({groupKey:_r.groupKey,title:_r.title,modelCount:_r.modelCount,blueCount:_r.blueCount,yellowCount:_r.yellowCount,redCount:_r.redCount,sortOrder:_r.sortOrder})

-<VirtualTable-VTWarningBars "vtWarningBars">.select(null,[["groupKey","asc"],["sortOrder","asc"]],[0,500],["groupKey","modelLabel","value","color","sortOrder"],null) -> _wBarResult
-_warningBars([{groupKey:STRING,modelLabel:STRING,value:INT,color:STRING,sortOrder:INT}]) = []
-IF _wBarResult.success
--FOR (_r,_i) IN _wBarResult.dataArray
---_warningBars.push({groupKey:_r.groupKey,modelLabel:_r.modelLabel,value:_r.value,color:_r.color,sortOrder:_r.sortOrder})

-_majorEvent({totalCount:INT,doneCount:INT,pctLabel:STRING,pctNum:INT}) = {totalCount:0,doneCount:0,pctLabel:"",pctNum:0}
-<VirtualTable-VTMajorEvents "vtMajorEvents">.select(null,null,[0,1],["totalCount","doneCount","pctLabel","pctNum"],null) -> _majorResult
-IF !_majorResult.success
--RETURN {success:false,message:"majorEvent load failed",orgStats:_orgStats,memberDonut:_memberDonut,collegeRatios:_collegeRatios,incubationProjects:_incubationProjects,cadreTabs:_cadreTabs,cadreGenders:_cadreGenders,cadreAges:_cadreAges,cadreTitles:_cadreTitles,orgKpis:_orgKpis,duesBars:_duesBars,sideJobSlices:_sideJobSlices,mediaRanks:_mediaRanks,mediaTable:_mediaTable,studyBars:_studyBars,opinionAreas:_opinionAreas,warningSummaries:_warningSummaries,warningBars:_warningBars,majorEvent:_majorEvent,platformMeta:{schoolCn:"",schoolEn:"",title:"",sideJobTotal:0}}
-IF _majorResult.dataArray.length > 0
--_majorEvent = {totalCount:_majorResult.dataArray[0].totalCount,doneCount:_majorResult.dataArray[0].doneCount,pctLabel:_majorResult.dataArray[0].pctLabel,pctNum:_majorResult.dataArray[0].pctNum}

-_platformMeta({schoolCn:STRING,schoolEn:STRING,title:STRING,sideJobTotal:INT}) = {schoolCn:"Lakeview University",schoolEn:"SMART CAMPUS · OPERATIONS CENTER",title:"Smart Campus Operations Dashboard",sideJobTotal:328}
-<VirtualTable-VTPlatformMeta "vtPlatformMeta">.select(null,null,[0,1],["schoolCn","schoolEn","title","sideJobTotal"],null) -> _metaResult
-IF !_metaResult.success
--RETURN {success:false,message:"platformMeta load failed",orgStats:_orgStats,memberDonut:_memberDonut,collegeRatios:_collegeRatios,incubationProjects:_incubationProjects,cadreTabs:_cadreTabs,cadreGenders:_cadreGenders,cadreAges:_cadreAges,cadreTitles:_cadreTitles,orgKpis:_orgKpis,duesBars:_duesBars,sideJobSlices:_sideJobSlices,mediaRanks:_mediaRanks,mediaTable:_mediaTable,studyBars:_studyBars,opinionAreas:_opinionAreas,warningSummaries:_warningSummaries,warningBars:_warningBars,majorEvent:_majorEvent,platformMeta:_platformMeta}
-IF _metaResult.dataArray.length > 0
--_platformMeta = {schoolCn:_metaResult.dataArray[0].schoolCn,schoolEn:_metaResult.dataArray[0].schoolEn,title:_metaResult.dataArray[0].title,sideJobTotal:_metaResult.dataArray[0].sideJobTotal}

-RETURN {success:true,message:"",orgStats:_orgStats,memberDonut:_memberDonut,collegeRatios:_collegeRatios,incubationProjects:_incubationProjects,cadreTabs:_cadreTabs,cadreGenders:_cadreGenders,cadreAges:_cadreAges,cadreTitles:_cadreTitles,orgKpis:_orgKpis,duesBars:_duesBars,sideJobSlices:_sideJobSlices,mediaRanks:_mediaRanks,mediaTable:_mediaTable,studyBars:_studyBars,opinionAreas:_opinionAreas,warningSummaries:_warningSummaries,warningBars:_warningBars,majorEvent:_majorEvent,platformMeta:_platformMeta}

# Backend Internal Methods
// Local previews start with empty tables: .vdb seed rows are not imported into the runtime.
// Generated from Database seed rows (internal _id/_user/_create/_update omitted); keep in sync.
METHOD ensureDemoData();RETURN {success:BOOL,seededTables:INT}
-_seededTables(INT) = 0
-<VirtualTable-VTOrgStats "vtOrgStats">.select([], null, [0,1], null, null) -> _orgStatsProbe
-IF !_orgStatsProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _orgStatsProbe.dataArray.length == 0
--<VirtualTable-VTOrgStats "vtOrgStats">.insertMulti([{"label":"Schools","value":24,"sortOrder":1},{"label":"Student Clubs","value":329,"sortOrder":2},{"label":"Research Centers","value":25,"sortOrder":3}]) -> _orgStatsSeed
--IF !_orgStatsSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTPartyMemberSlices "vtPartyMember">.select([], null, [0,1], null, null) -> _partyMemberSlicesProbe
-IF !_partyMemberSlicesProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _partyMemberSlicesProbe.dataArray.length == 0
--<VirtualTable-VTPartyMemberSlices "vtPartyMember">.insertMulti([{"label":"Students","value":6491,"color":"#25e8e0","showLegend":1,"sortOrder":1},{"label":"Faculty & Staff","value":1975,"color":"#ff5aa8","showLegend":1,"sortOrder":2},{"label":"Contractors","value":600,"color":"#ffd23a","showLegend":0,"sortOrder":3},{"label":"Visitors","value":380,"color":"#b06bff","showLegend":0,"sortOrder":4}]) -> _partyMemberSlicesSeed
--IF !_partyMemberSlicesSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTCollegeRatios "vtCollegeRatios">.select([], null, [0,1], null, null) -> _collegeRatiosProbe
-IF !_collegeRatiosProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _collegeRatiosProbe.dataArray.length == 0
--<VirtualTable-VTCollegeRatios "vtCollegeRatios">.insertMulti([{"label":"Student Attendance","currentVal":6491,"totalVal":23175,"pctLabel":"28.01%","pctNum":28,"color":"cyan","sortOrder":1},{"label":"Staff On Duty","currentVal":1975,"totalVal":2538,"pctLabel":"77.82%","pctNum":78,"color":"green","sortOrder":2}]) -> _collegeRatiosSeed
--IF !_collegeRatiosSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTIncubationProjects "vtIncubation">.select([], null, [0,1], null, null) -> _incubationProjectsProbe
-IF !_incubationProjectsProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _incubationProjectsProbe.dataArray.length == 0
--<VirtualTable-VTIncubationProjects "vtIncubation">.insertMulti([{"title":"Library Smart Seating Upgrade","level":"State","sortOrder":1},{"title":"Green Building Pilot","level":"Campus","sortOrder":2},{"title":"Faculty Mentorship Studio","level":"Campus","sortOrder":3},{"title":"Library Smart Seating Upgrade","level":"State","sortOrder":4},{"title":"Student Wellbeing Research Grant","level":"Campus","sortOrder":5}]) -> _incubationProjectsSeed
--IF !_incubationProjectsSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTCadreTabs "vtCadreTabs">.select([], null, [0,1], null, null) -> _cadreTabsProbe
-IF !_cadreTabsProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _cadreTabsProbe.dataArray.length == 0
--<VirtualTable-VTCadreTabs "vtCadreTabs">.insertMulti([{"tabKey":"mid","label":"Faculty","sortOrder":1},{"tabKey":"ke","label":"Staff","sortOrder":2},{"tabKey":"ss","label":"Researchers","sortOrder":3}]) -> _cadreTabsSeed
--IF !_cadreTabsSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTCadreGenders "vtCadreGenders">.select([], null, [0,1], null, null) -> _cadreGendersProbe
-IF !_cadreGendersProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _cadreGendersProbe.dataArray.length == 0
--<VirtualTable-VTCadreGenders "vtCadreGenders">.insertMulti([{"tabKey":"mid","label":"Male","value":65,"color":"#25e8e0","sortOrder":1},{"tabKey":"mid","label":"Female","value":35,"color":"#ff5aa8","sortOrder":2},{"tabKey":"ke","label":"Male","value":55,"color":"#25e8e0","sortOrder":1},{"tabKey":"ke","label":"Female","value":45,"color":"#ff5aa8","sortOrder":2},{"tabKey":"ss","label":"Male","value":60,"color":"#25e8e0","sortOrder":1},{"tabKey":"ss","label":"Female","value":40,"color":"#ff5aa8","sortOrder":2}]) -> _cadreGendersSeed
--IF !_cadreGendersSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTCadreAges "vtCadreAges">.select([], null, [0,1], null, null) -> _cadreAgesProbe
-IF !_cadreAgesProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _cadreAgesProbe.dataArray.length == 0
--<VirtualTable-VTCadreAges "vtCadreAges">.insertMulti([{"tabKey":"mid","label":"35 & under","value":18,"pctNum":18,"color":"#25e8e0","sortOrder":1},{"tabKey":"mid","label":"36-45","value":45,"pctNum":45,"color":"#2bf08a","sortOrder":2},{"tabKey":"mid","label":"46-55","value":25,"pctNum":25,"color":"#ffd23a","sortOrder":3},{"tabKey":"mid","label":"56 & over","value":12,"pctNum":12,"color":"#b06bff","sortOrder":4},{"tabKey":"ke","label":"35 & under","value":32,"pctNum":32,"color":"#25e8e0","sortOrder":1},{"tabKey":"ke","label":"36-45","value":38,"pctNum":38,"color":"#2bf08a","sortOrder":2},{"tabKey":"ke","label":"46-55","value":22,"pctNum":22,"color":"#ffd23a","sortOrder":3},{"tabKey":"ke","label":"56 & over","value":8,"pctNum":8,"color":"#b06bff","sortOrder":4},{"tabKey":"ss","label":"35 & under","value":25,"pctNum":25,"color":"#25e8e0","sortOrder":1},{"tabKey":"ss","label":"36-45","value":42,"pctNum":42,"color":"#2bf08a","sortOrder":2},{"tabKey":"ss","label":"46-55","value":23,"pctNum":23,"color":"#ffd23a","sortOrder":3},{"tabKey":"ss","label":"56 & over","value":10,"pctNum":10,"color":"#b06bff","sortOrder":4}]) -> _cadreAgesSeed
--IF !_cadreAgesSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTCadreTitles "vtCadreTitles">.select([], null, [0,1], null, null) -> _cadreTitlesProbe
-IF !_cadreTitlesProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _cadreTitlesProbe.dataArray.length == 0
--<VirtualTable-VTCadreTitles "vtCadreTitles">.insertMulti([{"tabKey":"mid","label":"Senior","value":18,"color":"#25e8e0","sortOrder":1},{"tabKey":"mid","label":"Associate","value":32,"color":"#ff5aa8","sortOrder":2},{"tabKey":"mid","label":"Mid-level","value":35,"color":"#ffd23a","sortOrder":3},{"tabKey":"mid","label":"Junior","value":15,"color":"#b06bff","sortOrder":4},{"tabKey":"ke","label":"Senior","value":8,"color":"#25e8e0","sortOrder":1},{"tabKey":"ke","label":"Associate","value":22,"color":"#ff5aa8","sortOrder":2},{"tabKey":"ke","label":"Mid-level","value":45,"color":"#ffd23a","sortOrder":3},{"tabKey":"ke","label":"Junior","value":25,"color":"#b06bff","sortOrder":4},{"tabKey":"ss","label":"Senior","value":28,"color":"#25e8e0","sortOrder":1},{"tabKey":"ss","label":"Associate","value":38,"color":"#ff5aa8","sortOrder":2},{"tabKey":"ss","label":"Mid-level","value":22,"color":"#ffd23a","sortOrder":3},{"tabKey":"ss","label":"Junior","value":12,"color":"#b06bff","sortOrder":4}]) -> _cadreTitlesSeed
--IF !_cadreTitlesSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTOrgKpis "vtOrgKpis">.select([], null, [0,1], null, null) -> _orgKpisProbe
-IF !_orgKpisProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _orgKpisProbe.dataArray.length == 0
--<VirtualTable-VTOrgKpis "vtOrgKpis">.insertMulti([{"label":"Opened","value":48,"color":"yellow","sortOrder":1},{"label":"Resolved","value":200,"color":"pink","sortOrder":2}]) -> _orgKpisSeed
--IF !_orgKpisSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTDuesBars "vtDuesBars">.select([], null, [0,1], null, null) -> _duesBarsProbe
-IF !_duesBarsProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _duesBarsProbe.dataArray.length == 0
--<VirtualTable-VTDuesBars "vtDuesBars">.insertMulti([{"monthLabel":"Jan","value":89,"sortOrder":1},{"monthLabel":"Feb","value":100,"sortOrder":2},{"monthLabel":"Mar","value":60,"sortOrder":3},{"monthLabel":"Apr","value":94,"sortOrder":4},{"monthLabel":"May","value":87,"sortOrder":5}]) -> _duesBarsSeed
--IF !_duesBarsSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTSideJobSlices "vtSideJob">.select([], null, [0,1], null, null) -> _sideJobSlicesProbe
-IF !_sideJobSlicesProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _sideJobSlicesProbe.dataArray.length == 0
--<VirtualTable-VTSideJobSlices "vtSideJob">.insertMulti([{"label":"Lectures","value":50,"percent":"50%","color":"#25e8e0","sortOrder":1},{"label":"Sports","value":25,"percent":"25%","color":"#ff5aa8","sortOrder":2},{"label":"Arts & Culture","value":20,"percent":"20%","color":"#2bf08a","sortOrder":3},{"label":"Other","value":1,"percent":"1%","color":"#ffd23a","sortOrder":4}]) -> _sideJobSlicesSeed
--IF !_sideJobSlicesSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTMediaRanks "vtMediaRanks">.select([], null, [0,1], null, null) -> _mediaRanksProbe
-IF !_mediaRanksProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _mediaRanksProbe.dataArray.length == 0
--<VirtualTable-VTMediaRanks "vtMediaRanks">.insertMulti([{"label":"Continuing Education","value":"8.1","barPct":16,"sortOrder":1},{"label":"Athletics Department","value":"6.9","barPct":13,"sortOrder":2},{"label":"International Programs","value":"50.95","barPct":100,"sortOrder":3},{"label":"School of Humanities","value":"21.42","barPct":42,"sortOrder":4},{"label":"Innovation & Entrepreneurship","value":"23.81","barPct":47,"sortOrder":5},{"label":"School of Languages","value":"26.19","barPct":51,"sortOrder":6},{"label":"Law, Policy & Journalism","value":"11.9","barPct":23,"sortOrder":7}]) -> _mediaRanksSeed
--IF !_mediaRanksSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTMediaTable "vtMediaTable">.select([], null, [0,1], null, null) -> _mediaTableProbe
-IF !_mediaTableProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _mediaTableProbe.dataArray.length == 0
--<VirtualTable-VTMediaTable "vtMediaTable">.insertMulti([{"platform":"Instagram","postCount":"178","readCount":"1.37M","sortOrder":1},{"platform":"LinkedIn","postCount":"3200","readCount":"56M","sortOrder":2},{"platform":"YouTube","postCount":"45","readCount":"2.32M","sortOrder":3},{"platform":"TikTok","postCount":"61","readCount":"1.1M","sortOrder":4},{"platform":"Bilibili","postCount":"45","readCount":"60K","sortOrder":5}]) -> _mediaTableSeed
--IF !_mediaTableSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTStudyBars "vtStudyBars">.select([], null, [0,1], null, null) -> _studyBarsProbe
-IF !_studyBarsProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _studyBarsProbe.dataArray.length == 0
--<VirtualTable-VTStudyBars "vtStudyBars">.insertMulti([{"label":"Materials","annualVal":5,"monthlyVal":2,"sortOrder":1},{"label":"Design","annualVal":2,"monthlyVal":5,"sortOrder":2},{"label":"Computing","annualVal":8,"monthlyVal":2,"sortOrder":3},{"label":"Engineering","annualVal":5,"monthlyVal":4,"sortOrder":4},{"label":"Info Science","annualVal":5,"monthlyVal":4,"sortOrder":5},{"label":"Business","annualVal":5,"monthlyVal":4,"sortOrder":6}]) -> _studyBarsSeed
--IF !_studyBarsSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTOpinionAreas "vtOpinionAreas">.select([], null, [0,1], null, null) -> _opinionAreasProbe
-IF !_opinionAreasProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _opinionAreasProbe.dataArray.length == 0
--<VirtualTable-VTOpinionAreas "vtOpinionAreas">.insertMulti([{"ageLabel":"Dining","partyVal":42,"disciplineVal":35,"sortOrder":1},{"ageLabel":"Housing","partyVal":75,"disciplineVal":62,"sortOrder":2},{"ageLabel":"Library","partyVal":58,"disciplineVal":68,"sortOrder":3},{"ageLabel":"IT Services","partyVal":72,"disciplineVal":58,"sortOrder":4}]) -> _opinionAreasSeed
--IF !_opinionAreasSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTWarningSummaries "vtWarningSummaries">.select([], null, [0,1], null, null) -> _warningSummariesProbe
-IF !_warningSummariesProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _warningSummariesProbe.dataArray.length == 0
--<VirtualTable-VTWarningSummaries "vtWarningSummaries">.insertMulti([{"groupKey":"fangchan","title":"Building Energy Monitoring","modelCount":42,"blueCount":13,"yellowCount":152,"redCount":7,"sortOrder":1},{"groupKey":"keyanan","title":"Lab Safety","modelCount":29,"blueCount":13,"yellowCount":152,"redCount":7,"sortOrder":2}]) -> _warningSummariesSeed
--IF !_warningSummariesSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTWarningBars "vtWarningBars">.select([], null, [0,1], null, null) -> _warningBarsProbe
-IF !_warningBarsProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _warningBarsProbe.dataArray.length == 0
--<VirtualTable-VTWarningBars "vtWarningBars">.insertMulti([{"groupKey":"fangchan","modelLabel":"Zone 1","value":62,"color":"#ffd23a","sortOrder":1},{"groupKey":"fangchan","modelLabel":"Zone 2","value":46,"color":"#ffd23a","sortOrder":2},{"groupKey":"fangchan","modelLabel":"Zone 3","value":40,"color":"#ffd23a","sortOrder":3},{"groupKey":"fangchan","modelLabel":"Zone 4","value":38,"color":"#ffd23a","sortOrder":4},{"groupKey":"fangchan","modelLabel":"Zone 5","value":32,"color":"#ffd23a","sortOrder":5},{"groupKey":"fangchan","modelLabel":"Zone 6","value":28,"color":"#ffd23a","sortOrder":6},{"groupKey":"fangchan","modelLabel":"Zone 7","value":24,"color":"#ffd23a","sortOrder":7},{"groupKey":"fangchan","modelLabel":"Zone 8","value":18,"color":"#ff5b6e","sortOrder":8},{"groupKey":"fangchan","modelLabel":"Zone 9","value":16,"color":"#ff5b6e","sortOrder":9},{"groupKey":"fangchan","modelLabel":"Zone 10","value":9,"color":"#ff5b6e","sortOrder":10},{"groupKey":"keyanan","modelLabel":"Zone 1","value":60,"color":"#ffd23a","sortOrder":1},{"groupKey":"keyanan","modelLabel":"Zone 2","value":42,"color":"#ffd23a","sortOrder":2},{"groupKey":"keyanan","modelLabel":"Zone 3","value":36,"color":"#ffd23a","sortOrder":3},{"groupKey":"keyanan","modelLabel":"Zone 4","value":32,"color":"#ffd23a","sortOrder":4},{"groupKey":"keyanan","modelLabel":"Zone 5","value":28,"color":"#ffd23a","sortOrder":5},{"groupKey":"keyanan","modelLabel":"Zone 6","value":24,"color":"#ffd23a","sortOrder":6},{"groupKey":"keyanan","modelLabel":"Zone 7","value":20,"color":"#ffd23a","sortOrder":7},{"groupKey":"keyanan","modelLabel":"Zone 8","value":17,"color":"#ff5b6e","sortOrder":8},{"groupKey":"keyanan","modelLabel":"Zone 9","value":12,"color":"#ff5b6e","sortOrder":9},{"groupKey":"keyanan","modelLabel":"Zone 10","value":8,"color":"#ff5b6e","sortOrder":10}]) -> _warningBarsSeed
--IF !_warningBarsSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTMajorEvents "vtMajorEvents">.select([], null, [0,1], null, null) -> _majorEventsProbe
-IF !_majorEventsProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _majorEventsProbe.dataArray.length == 0
--<VirtualTable-VTMajorEvents "vtMajorEvents">.insertMulti([{"totalCount":320,"doneCount":270,"pctLabel":"84.38%","pctNum":84}]) -> _majorEventsSeed
--IF !_majorEventsSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-<VirtualTable-VTPlatformMeta "vtPlatformMeta">.select([], null, [0,1], null, null) -> _platformMetaProbe
-IF !_platformMetaProbe.success
--RETURN {success:false,seededTables:_seededTables}
-IF _platformMetaProbe.dataArray.length == 0
--<VirtualTable-VTPlatformMeta "vtPlatformMeta">.insertMulti([{"schoolCn":"Lakeview University","schoolEn":"SMART CAMPUS · OPERATIONS CENTER","title":"Smart Campus Operations Dashboard","sideJobTotal":328}]) -> _platformMetaSeed
--IF !_platformMetaSeed.success
---RETURN {success:false,seededTables:_seededTables}
--_seededTables = _seededTables + 1
-RETURN {success:true,seededTables:_seededTables}

</ServiceDomain-Dashboard>
