/**
 * Created by Liz on 11/16/2015.
 */
var colors = ['red', 'blue', 'black', 'green', 'yellow', 'gold', 'purple', 'multi'];
var ms_number = ['2I','2II','2III','3','4','9','10','11','12','16I','16II','17','22','23','26',
    '27','28','29','30','31','33','41','42','44','46','47','48','49','50','51','52','54','55','58',
    '62','65','66','66A','67','71','72','75','83','86','87','89','92','94','107','111','130','131',
    '134','135','136','139','140','146','149','150','160','161','162','163','164','178','184','186',
    '187','188','190','191','196','198','199','200','201','202','204','212','214','219','222','226',
    '228','229','230','231','236','246','252','253','262','263','265','266','267','269','270','271',
    '273','274','275','276','277','280','281','288','289','290','291','292','294','295','299','300',
    '302','303','308','309','310','312','313','315','316','317','318','319','320','321','322','327',
    '328','330','332','337','339','345','356','361','364','366','367','371','373','375','376','380',
    '383','385','390','393','397','400','402','404','405','406','415','416','419','421','422','424',
    '425','433','437','438','439','441','442','449','451','452','455','457','459','461','462','463',
    '466','468','469','470','473','475','478','480','481','483','484','485','486','505','511','628'];
var centuries = ['9','10','11','12','13','14','15','16'];
var super_scripts = ['in','1','2','med','ex'];
var regions = [''];

function getModule(index){
    var search_module = "<div class='option'>" +
                        "<div class='row'>" +
                            "<div class='six columns'>" +
                                "<!-- MANUSCRIPT -->" +
                                "<label for='ms-"+index+"'>Manuscript</label>" +
                                "<select name='manuscript' id='ms-"+index+"'>" +
                                    "<option value=''></option>";
                                    for (var n in ms_number){
                                        search_module += "<option value='"+ms_number[n]+"'>"+ms_number[n]+"</option>";
                                    }
              search_module += "</select>" +
                            "</div>" +
                            "<div class='six columns'>" +
                            "<!-- DATE -->" +
                                "<label for='century-"+index+"'>Date</label>" +
                                "<select name='century' class='century' id='century-"+index+"'>" +
                                    "<option value=''></option>";
                                    for (var cent in centuries){
                                        search_module += "<option value='"+centuries[cent]+"'>"+centuries[cent]+"</option>";
                                    }
              search_module += "</select>" +
                                "<select name='super' class='super' id='super-"+index+"'>" +
                                    "<option value=''></option>";
                                    for (var s in super_scripts){
                                        search_module += "<option value='"+super_scripts[s]+"'>"+super_scripts[s]+"</option>";
                                    }
              search_module += "</select>" +
                            "</div>" +
                        "</div>" +
                    "<div class='row'>" +
                        "<div class='six columns'>" +
                            "<!-- LOCATION -->  " +
                            "<label for='location-"+index+"'>Location</label>" +
                            "<input type='text' name='folio-num' id='location-"+index+"' placeholder='Christ Church'>" +
                        "</div>" +
                        "<div class='six columns'>" +
                            "<!-- REGION -->" +
                            "<label for='region-"+index+"'>Region</label>" +
                            "<select name='region' id='region-"+index+"'>" +
                                "<option value=''></option>";
                                for (var r in regions){
                                    search_module += "<option value='"+r+"'>"+r+"</option>";
                                }
          search_module += "</select>" +
                        "</div>" +
                    "</div>" +
                    "<div class='row'>" +
                        "<div class='six columns'>" +
                            "<!-- FOLIO -->" +
                            "<label for='folio-"+index+"'>Folio</label>" +
                            "<input type='text' name='folio-num' id='folio-"+index+"' placeholder='15 R, 103 V'>" +
                    "</div>" +
                    "<div class='six columns'>" +
                        "<!-- FEATURE -->" +
                        "<label for='feature-"+index+"'>Feature</label>" +
                        "<select name='feature-select'>" +
                            "<option value = 'ln'>Litterae Notabiliores</option>" +
                            "<option value = 'ec'>Enlarged Capitals</option>" +
                            "<option value = 'rubric'>Rubrics</option>" +
                        "</select>" +
                    "</div>" +
                "</div>" +
                "<div class='row'>" +
                    "<div class='six columns'>" +
                        "<!-- PRIMARY COLOR -->" +
                        "<label for='p-color-"+index+"'>Primary Color</label>" +
                        "<select name='primary-color' id='primary-color-"+index+"'>";
                            for (var pcolor in colors){
                                search_module += "";
                            }
      search_module += "</select>" +
                "</div>" +
                "<div class='six columns'>" +
                    "<!-- SECONDARY COLOR -->" +
                    "<label for='s-color-"+index+"'>Secondary Color</label>" +
                        "<select name='secondary-color' id='s-color-"+index+">";
                            for (var scolor in colors){
                                search_module += "";
                            }
      search_module += "</select>" +
                    "</div>" +
                "</div>";
    search_module += "</div>";

    return search_module;
}

function toTitleCase(str) {
    return str.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
}


$(document).ready(function() {
    var intID = 0;
    $("#add").click(function() {
        var wrapper = $("<div class='option'></div>");

        var r1 = $("<div class='row'></div>");
        var removeButton = $("<input class='remove' value='x' type='button'>");
        removeButton.click(function() {
            $(this).closest("div .option").remove();
        });
        $(r1).append(removeButton);

        var stuff = $(getModule(intID));
        intID += 1;

        $(stuff).prepend(r1);

        $("#feature-search-wrapper").append(stuff);
    });
});
