/**
 * Created by liz on 2/1/16.
 */

/* *********
   Constants
   ********* */
var features = [
    {'shorthand':'LN', 'human':'Litterae Notabiliores'},
    {'shorthand':'EC', 'human':'Enlarged Capitals'},
    {'shorthand':'RB', 'human':'Rubrics'},
    {'shorthand':'IS', 'human':'Intertextual Space'}];
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
var super_scripts = ['', 'in','1','2','med','ex']; //TODO make acutal superscript? Object the "normal" to codes?
var regions = ['North West England', 'North East England', 'Yorkshire and the Humber', 'Wales', 'West Midlands',
    'East Midlands', 'South West England', 'South East England', 'London', 'East of England', 'Italy', 'Germany',
    'France'];
var letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'];
var lnclasses = [
    {'shorthand':'L', 'human':'Large & Intricate'},
    {'shorthand':'I', 'human':'Intricate'},
    {'shorthand':'M', 'human':'Multi-colored'},
    {'shorthand':'D', 'human':'Dual-colored'},
    {'shorthand':'S', 'human':'Single-colored'}];
var LN_EC_errors = [
    {'shorthand':'MC', 'human':'Multiple caught'},
    {'shorthand':'NL', 'human':'Non-letter'},
    {'shorthand':'PT', 'human':'Partial'},
    {'shorthand':'IN', 'human':'Incorrect feature'}];
var IS_errors = [
    {'shorthand':'1', 'human':'Physical element'},
    {'shorthand':'2', 'human':'Textual element'}];

/* ***************************
   Form field getter functions
   *************************** */
function getMSFields(index) {
    var ms =  "<!-- MANUSCRIPT -->" +
        "<div class='ms' id='ms-"+index+"'>"+
            "<label for='ms-"+index+"'>Manuscript</label>" +
            "<select multiple name='manuscript' id='ms-"+index+"'>" +
                 "<option value='' selected>all</option>";
                    for (var n in ms_number){
                        ms += "<option value='"+ms_number[n]+"'>"+ms_number[n]+"</option>";
                    }
    ms += "</select>"+
        "</div>";
    return ms;
}
function getDateFields(index) {
   var date = "<!-- DATE -->" +
   "<div class='date' id='date-"+index+"'>"+
        "<label for='century-"+index+"'>Date</label>" +
        "<select multiple name='century' class='century' id='century-"+index+"'>" +
            "<option value='' selected>all</option>";
            for (var cent in centuries){
                date += "<option value='"+centuries[cent]+"'>" + centuries[cent]+"</sup></option>";
                /*for (var s in super_scripts){
                    date += "<option value='"+centuries[cent]+"-"+super_scripts[s]+"'>" +
                    centuries[cent]+"<sup> "+super_scripts[s]+"</sup></option>";
                }*/
            }
        date += "</select>"
            +"</div>";

    return date;
}
function getRegionFields(index) {
    var region =  "<!-- REGION -->" +
        "<div class='region' id='region-"+index+"'>"+
        "<label for='region-"+index+"'>Region</label>" +
        "<select multiple name='region' id='region-"+index+"'>" +
        "<option value='' selected>any</option>";
        for (var r in regions){
            region += "<option value='"+regions[r]+"'>"+regions[r]+"</option>";
        }
    region += "</select>"+
        "</div>";
    return region;
}
function getErrorFields(index, type){
    var html = "<input type='checkbox' id='error-"+index+"' name='error-"+index+"' onclick=\"showMe('error-"+index+"')\"" +
        " value='error'>Include Errors<br>"
        // Not Rubrics
        if (type != features[3].shorthand) {
            html += "<div class='errorType' id='errorType-" + index + "'style='display: none;'>" +
                "<label for=''></label>" +
                "<select multiple name='errorSelect' id='errorSelect-" + index + "'>" +
                "<option value='' selected>all</option>";
            // LN or EC Error Types
            if (type == features[0].shorthand || type == features[1].shorthand) {
                for (var e in LN_EC_errors) {
                    html += "<option value'" + LN_EC_errors[e].shorthand + "'>" + LN_EC_errors[e].human + "</option>";
                }
            }
            // IS Error Types
            else if (type == features[2].shorthand) {
               for (var e in IS_errors) {
                    html += "<option value'" + IS_errors[e].shorthand + "'>" + IS_errors[e].human + "</option>";
                }
            }
            html += "</select>" +
                "</div>";
        }
    return html;
}
function showMe (boxID) {
    var index = boxID.split("-")[1]
    var checkbox = document.getElementById(boxID);
    var vis = "none";
    if(checkbox.checked){
        vis = "block";
    }
    document.getElementById("errorType-"+index).style.display = vis;
}
function getColorFields(index) {
    var color_html = "<!-- COLORS -->" +
        "<div class='color' id='color-"+index+"'>"+
        "<label for='pcolor-"+index+"'>Main Color</label>" +
        "<select name='pcolor' class='pcolor' id='pcolor-"+index+"'>" +
        "<option value=''>any</option>";
            for (var c in colors){
                color_html += "<option value='"+colors[c]+"'>"+colors[c]+"</option>";
            }
    color_html += "</select>" +
        "<label for='scolor-"+index+"'>Secondary Colors</label>" +
        "<select multiple name='scolor' class='scolor' id='scolor-"+index+"'>" +
            "<option value=''>any</option> <option value='NULL'>none</option> ";
            for (var c in colors){
                color_html += "<option value='"+colors[c]+"'>"+colors[c]+"</option>";
            }
    color_html += "</select>"
        +"</div>";

    return color_html;
}
function getLetterFields(index) {
    var letter =  "<!-- REGION -->" +
        "<div class='letter' id='letter-"+index+"'>"+
        "<label for='letter-"+index+"'>Letter</label>" +
        "<select multiple name='letter' id='letter-"+index+"'>" +
        "<option value='' selected>any</option>";
    for (var l in letters){
        letter += "<option value='"+letters[l]+"'>"+letters[l]+"</option>";
    }
    letter += "</select>"+
        "</div>";
    return letter;
}
function getLNClassFields(index) {
    var lnclass =  "<!-- LN CLASS -->" +
        "<div class='lnclass' id='lnclass-"+index+"'>"+
        "<label for='lnclass-"+index+"'>Class</label>" +
        "<select multiple name='lnclass' id='lnclass-"+index+"'>" +
        "<option value='' selected>any</option>";
        for (var c in lnclasses){
            lnclass += "<option value='"+lnclasses[c].shorthand+"'>"+lnclasses[c].human+"</option>";
        }
    lnclass += "</select>"+
        "</div>";

    return lnclass;
}

function getLNModule(index) {
    var color = getColorFields(index);
    var letter = getLetterFields(index);
    var lnclass = getLNClassFields(index);

    return color+letter+lnclass;
}
function getECModule(index){
    var color = getColorFields(index);
    var letter = getLetterFields(index);

    var html = color+letter;
    return color+letter;
}

function getModule(type, index) {
    var ms = getMSFields(index);
    var date = getDateFields(index);
    var region = getRegionFields(index);
    var error = getErrorFields(index, type);

    var featureSpecific;
    switch (type) {
        case features[0].shorthand:
            featureSpecific = getLNModule(index);
            break;
        case features[1].shorthand:
            featureSpecific = getECModule(index);
            break;
        default:
            featureSpecific = "";
    }

    return ms+date+region+featureSpecific+error;
}

/* ****************************
   Feature select functionality
   **************************** */
$(document).ready(function() {
    for (var i in features){
        var f = features[i];
        $('#feature-type').append("<option value='"+ f.shorthand+"'>"+ f.human +"</option>");
    }

    var intID = 0;
    $("#add").click(function() {
        var selected_index = document.getElementById("feature-type").selectedIndex;
        var feature_type = document.getElementById("feature-type").options[selected_index].value;
        var feature_short = features[selected_index].shorthand;

        var module = getModule(feature_type, intID);

        var wrapper = $("<div class='feature' data-feature='"+feature_short+"'></div>");

        var removeButton = $("<input class='remove' value='x' type='button'>");
        removeButton.click(function() {
            $(this).closest("div .feature").remove();
        });
        $(wrapper).append(removeButton);
        $(wrapper).append(module);

        intID += 1;

        $("#feature-search-wrapper").append(wrapper);
    });
});