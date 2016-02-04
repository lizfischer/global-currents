<?php
function input_value($x){
    if (isset($_GET[$x])) {
        return $_GET[$x];
    }
    else {
        return '';
    }
}
?>

<ul class="nav">
    <form action="index.php" method="get">
        <div class="option">
            <h2>Manuscript: </h2>
            <select name="manuscript">
                <option value=''></option>
                <?php

                foreach ($ms_number as $n){
                    $msInput = "<option value='".$n."'";
                    if($_GET['manuscript'] == $n) $msInput .= " selected = 'selected' ";
                    $msInput .= ">".$n."</option>";
                    echo $msInput;
                }
                ?>
            </select>
        </div>

        <div class="option">
            <h2>Folio</h2>
            <input type="text" name="folio-num" value="<?php echo $_GET["folio-num"]?>"> <br>
            <input type="radio" name="folio-rvp" value="R"
                <?php echo (input_value('folio-rvp') == 'R') ? 'checked="checked"' : ''; ?>>R
            <input type="radio" name="folio-rvp" value="V"
                <?php echo (input_value('folio-rvp') == 'V') ? 'checked="checked"' : ''; ?>>V
            <input type="radio" name="folio-rvp" value=""
                <?php echo (input_value('folio-rvp') == '') ? 'checked="checked"' : ''; ?>> Page
        </div>

        <div class="option">
            <h2>Feature</h2> <br><br>
            <input type="checkbox" name="ln" value="T"
                <?php echo (input_value('ln') == 'T') ? 'checked="checked"' : ''; ?>>
                Litterae Notabiliores <br>
            <input type="checkbox" name="ec" value="T"
                <?php echo (input_value('ec') == 'T') ? 'checked="checked"' : ''; ?>>
                Enlarged Capitals <br>
            <input type="checkbox" name="rubric" value="T"
                <?php echo (input_value('rubric') == 'T') ? 'checked="checked"' : ''; ?>>
                Rubrics <br>
        </div>

        <div class="option">
            <h2>Primary Color</h2> <br><br>
            <?php
            $color = array('red', 'blue', 'black', 'green', 'yellow', 'gold', 'purple', 'multi');
            for($i=0; $i < count($color); $i++){
                $colorInput = "<input type='checkbox' name='p-color[]' value='".$color[$i]."' ";
                if (in_array($color[$i], $_GET["p-color"], false)) $colorInput .= 'checked="checked"';

                $colorInput .= ">".ucwords($color[$i])."\n";
                echo $colorInput;
                if ($i % 2 == 1) echo "<br>";
            }
            ?><br>

            <input type="radio" name="p-color-restrict" value="any" checked="checked"> Match any
            <!--<input type="radio" name="p-color-restrict" value="all"> Match all-->
        </div>

        <div class="option">
            <h2>Secondary Colors</h2> <br><br>
            <?php
            for($i=0; $i < count($color); $i++){
                echo "<input type='checkbox' name='s-color[]' value='".$color[$i]."'>".ucwords($color[$i])."\n";
                if ($i % 2 == 1) echo "<br>";
            }
            ?><br>

            <input type="radio" name="s-color-restrict" value="any" checked="checked"> Match any
            <input type="radio" name="s-color-restrict" value="all"> Match all
        </div>

        <input class="button-primary" type="submit" name="submit" value="Search">
    </form>
</ul>