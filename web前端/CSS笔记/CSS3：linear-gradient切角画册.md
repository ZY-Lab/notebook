### css部分

```
.tucked-corners-top {
            position: relative;
            width: 500px;
            min-height: 200px;
            margin: 100px auto;
            padding: 20px;
            background-color: #fff;
            background:
                    -webkit-linear-gradient(45deg, transparent 10px, #fff 10px),
                    -webkit-linear-gradient(135deg, transparent 10px, #fff 10px),
                    -webkit-linear-gradient(225deg, transparent 10px, #fff 10px),
                    -webkit-linear-gradient(315deg, transparent 10px, #fff 10px);
            background-position: bottom left, bottom right, top right, top left;
            background-size: 55% 55%;
            background-repeat: no-repeat;
            box-shadow: 0 20px 10px -20px rgba(0, 0, 0, .5);
        }
        [class*='tucked-corners-']::before,
        [class*='tucked-corners-']::after {
            content: '';
            position: absolute;
            height: 20px; width: 80px;
            box-shadow: 0 8px 15px -7px rgba(0, 0, 0, .5);
            box-shadow: none\9; /* IE9 */
        }
        .tucked-corners-top::before,
        .tucked-corners-top::after {
            top: -10px;
        }
        .tucked-corners-bottom::before,
        .tucked-corners-bottom::after {
            bottom: -10px;
        }
        .tucked-corners-top::before,
        .tucked-corners-bottom::before {
            left: -42px;
        }
        .tucked-corners-top::after,
        .tucked-corners-bottom::after {
            right: -42px;
        }
        .tucked-corners-top::before {
            transform: rotate(-45deg);
        }
        .tucked-corners-top::after {
            transform: rotate(45deg);
        }
        .tucked-corners-bottom::before {
            transform: rotate(-135deg);
        }
        .tucked-corners-bottom::after {
            transform: rotate(135deg);
        }

```

### html部分
```
<div class="tucked-corners-top">
    <div class="tucked-corners-bottom"><img src="......" width="450"></div>
</div>
```