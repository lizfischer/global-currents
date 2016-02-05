<?php
$ms_numbers = array('2I','2II','2III','3','4','9','10','11','12','16I','16II','17','22','23','26',
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
    '466','468','469','470','473','475','478','480','481','483','484','485','486','505','511','628');
$centuries = array('9','10','11','12','13','14','15','16');
$super_scripts = array('','in','1','2','med','ex');
$colors = array ('red', 'blue', 'black', 'green', 'yellow', 'gold', 'purple', 'multi');
$regions = array ();

function getSearchModule($removeable, $index){
    global $ms_numbers, $centuries, $super_scripts, $colors, $regions;
    $search_module = "<div class='option'>
                        <div class='row'>
                            <div class='six columns'>
                                <!-- MANUSCRIPT -->
                                <label for='ms-".$index."'>Manuscript</label>
                                <select name='manuscript' id='ms-".$index."'>
                                    <option value=''></option>";
                                    foreach ($ms_numbers as $n){
                                        $search_module .= "<option value='".$n."'>".$n."</option>";
                                    }
             $search_module .= "</select>
                            </div>
                            <div class='six columns'>
                                <!-- DATE -->
                                <label for='century-".$index."'>Date Range</label>
                                <select name='century' class='century' id='century-".$index."'>
                                    <option value=''></option>";
                                    foreach ($centuries as $n){
                                        $search_module .= "<option value='".$n."'>".$n."</option>";
                                    }
             $search_module .= "</select>
                                <select name='super' class='super' id='super-".$index."'>
                                    <option value=''></option>";
                                    foreach ($super_scripts as $super){
                                        $search_module .= "<option value='".$super."'>".$super."</option>";
                                    }

             $search_module .= "</select>
                            </div>
                        </div>

                        <div class='row'>
                            <div class='six columns'>
                                <!-- LOCATION -->
                                <label for='location-".$index."'>Location</label>
                                <input type='text' name='folio-num' id='location-".$index."' placeholder='Christ Church'>
                            </div>
                            <div class='six columns'>
                                <!-- REGION -->
                                <label for='region-".$index."'>Region</label>
                                <select name='region' id='region-".$index."'>
                                    <option value=''></option>";
                                    foreach ($regions as $r){
                                        $search_module .= "<option value='".$r."'>".$r."</option>";
                                    }
             $search_module .= "</select>
                            </div>
                        </div>

                        <div class='row'>
                            <div class='six columns'>
                                <!-- FOLIO -->
                                <label for='folio-".$index."'>Folio</label>
                                <input type='text' name='folio-num' id='folio-".$index."' placeholder='15 R, 103 V'>
                            </div>
                            <div class='six columns'>
                                <!-- FEATURE -->
                                <label for='feature-".$index."'>Feature</label>
                                <select name='feature-select'>
                                    <option value = 'ln'>Litterae Notabiliores</option>
                                    <option value = 'ec'>Enlarged Capitals</option>
                                    <option value = 'rubric'>Rubrics</option>
                                </select>
                            </div>
                        </div>

                        <div class='row'>
                            <div class='six columns'>
                                <!-- PRIMARY COLOR -->
                                <label for='p-color-".$index."'>Primary Color</label>
                                <select name='primary-color'>";
                                    foreach ($colors as $c){
                                        $search_module .= "";
                                    }
             $search_module .= "</select>
                            </div>
                            <div class='six columns'>
                                <!-- SECONDARY COLOR -->
                                <label for='s-color-".$index."'>Secondary Color</label>
                                <select name='secondary-color'>";
                                    foreach ($colors as $c){
                                        $search_module .= "";
                                    }
             $search_module .= "</select>
                            </div>
                        </div>";

                if ($removeable){
                    $search_module .= "<input class='remove' value='remove' type='button'>";
                }
          $search_module.= "</div>";

    return $search_module;
}