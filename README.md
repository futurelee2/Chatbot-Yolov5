<div align= "center">
  <img width="850" src="https://i.esdrop.com/d/f/CcSudjZ5R8/permf9tpHa.png">
</div>
<br>
<br>


<h2> π νλ‘μ νΈ κ°μ </h2>

<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/Tov2sHONfa.png">
</div>
<br>

2021λ κΈ°μ€ 1μΈκ°κ΅¬μ μλ μ μ²΄ μΈκ΅¬μ 33.4%λ‘ μ½ 700λ§ κ°κ΅¬μλλ€.
κ·Έλ¦¬κ³  5λκ° 1μΈκ°κ΅¬μ λΉμ¨μ΄ λ§€λ μ¦κ°νκ³  μμμ νμΈ ν  μ μμ΅λλ€.

1μΈκ°κ΅¬κ° κ²ͺλ μ²« λ²μ§Έ μ΄λ €μμ μ¬λ¦¬μ  λΆμκ°κ³Ό μΈλ‘μμ΄κ³ , λ λ²μ§Έλ μν λμ λ³΄νΈμμ λΆμ¬μλλ€. 
μ΄μ²λΌ μ μμ  κ²°νμ΄ μ°μΈμ¦μΌλ‘ λ°μ λκ±°λ, λμμ¬κ³ μ²λΌ μκΈμ²μ§κ° νμν μν©μμ λμμ λ°μ§ λͺ»ν΄ κ³ λμ¬λ‘ μ΄μ΄μ§λ κ²½μ°κ° μμ΅λλ€.


μμ μ€λͺν λ°°κ²½μ ν λλ‘ νλ‘μ νΈμ λͺ©μ μ ν¬κ² λ κ°μ§λ‘ λλ΄μ΅λλ€.
μ²«μ§Έλ <μ±λ΄>μ ν΅ν΄ μ²­λμκ²λ κ²©λ €μ μμμ λ©μΈμ§λ₯Ό, λΈλμκ²λ λ§λ²μ΄ λμ΄μ£Όμ΄ 1μΈκ°κ΅¬μ μ°μΈμ¦μ κ°μ ν΄μ£Όκ³ ,
μ±λ΄μ μλ ₯ν λ©μμ§μμ μ¬κ°ν λΆμμ¦μΈκ° λ³΄μΌ κ²½μ°, μ§μΈμκ² μκΈμν©μ μλ €μ£Όμ΄ λμμ μμ²­νλ κ²μλλ€.

λμ§Έλ κ°κ΅¬ λ΄ νμ¬ λλ λμμ΄ λ°μ ν  κ²½μ° βμΉ΄μΉ΄μ€ν‘β μλ¦ΌμλΉμ€λ₯Ό ν΅ν΄ μ μνκ² λμ²ν  μ μλλ‘ λμμ£Όκ³ ,
μ₯μκ° μ§μ λΉμ μ λ μ€μκ° νμΈμ ν΅ν 1μΈκ°κ΅¬μ μ¬μ©μμ λΆμκ° ν΄μκ° λͺ©μ μλλ€.

<br>
<br>

<h2> πμ½λ μ€ν </h2>

```python
pip install -r requirements.txt
```

<h5> μ±λ΄ νμ΅ </h5>

```python
# python train_torch.py --train --gpus 1 --max_epochs 15
```
<h6> ν΄λΉ μ½λλ₯Ό ν΅ν΄ λ°μ΄ν°λ₯Ό νμ΅μμΌ CheckPointλ₯Ό λ§λ€μ΄λλλ€.<br><br>
     λ§λ  CheckPointλ --chat λͺλ Ήμ΄λ₯Ό μ¬μ©νλλ° μ΄μ©λ©λλ€. <br><br><br>
</h6> 

<h5> YOLO νμ΅ </h5>

```python
python ./Yolov5/train.py --data ./fall_dataset/data.yaml --epochs 100 --weights ./yolov5s.pt --batch-size 64 --img 640
```

<h6> ν΄λΉ μ½λλ₯Ό μλ ₯νλ©΄ μ½λμ λ€μ΄μλ κ·μΉμ λ§λ.pt νμΌμ λ§λ€μ΄μ€λλ€.<br><br>
     --data μλ λ³ΈμΈλ€μ΄ μ¬μ©ν  μ΄λ―Έμ§ λ°μ΄ν°μκ³Ό λΌλ²¨λ‘ κ΅¬μ±λ .yamlνμΌ μ΄λ¦μ λ£μ΄μ£Όλ©΄ λ©λλ€. <br><br>
     --weightλ κΈ°μ‘΄μ Pre-Trained λͺ¨λΈλ‘, λ€μν λͺ¨λΈμ΄ μμ§λ§ ν΄λΉ νλ‘μ νΈλ μ€μκ° κ°μ§κ° κ°μ₯ μ£Όκ° λκΈ° λλ¬Έμ, yolov5s.ptλ₯Ό μ¬μ©νμ΅λλ€.<br><br><br>
</h6>
     
     

<h5> μΉμ¬μ΄νΈλ‘ λ€μ΄κ°κΈ° </h5>



```python
if __name__ == '__main__':
    # app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
    app.run(host="0.0.0.0", debug=True, port=int(os.environ.get("PORT", 5000)))
```

<h6> app_flask_chatbot.py λ΄μ μ½λλ‘, Flaskλ₯Ό ν΅ν μΉμ¬μ΄νΈκ° μμ±λ©λλ€. <br><br>
     μΉμ¬μ΄νΈλ ν΄λΉ λ νΌμ§ν λ¦¬μ Templetes, static ν΄λ λ΄μ νμΌμ μμ νμ¬ μμ ν  μ μμ΅λλ€. <br><br>
     μ¬μ΄νΈ λ΄μ μλ κ° μΉ΄νκ³ λ¦¬μ μ¬μ§μ λλ₯΄κ² λλ©΄ μ±λ΄ λλ μ€μκ° κ°μ§μ°½μΌλ‘ λμ΄κ°κ² λ©λλ€. <br><br><br>
</h6>


<h2> π­ μλ‘ν μ±λ΄ : νμ°λ¦¬ </h2>

  <p>
<div>

<details>
<summary><b>νκ²½ λ° λ°μ΄ν°μ</b></summary>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/zDcvLE5rBt.png">
</div>
  <h5>κ΅¬μΆ νκ²½ </h5>
  <h6>Python 3.8 / Google Colab </h6>
  <h5>λ°μ΄ν°μ</h5>
  <h6>μ±λ΄μ λ°μ΄ν°μμ <'AI HUB'μ κ°μ± λν λ§λ­μΉ>μ <μ°λμ€ μ±λ΄ λ°μ΄ν°> 2κ°μ§λ₯Ό νμ©νμ¬ λ°μ΄ν°μμ κ΅¬μ±νμ΅λλ€.<br><br>
      λ°μ΄ν°μμ μ΄ 3κ°μ λΌλ²¨λ‘ κ΅¬μ±λμ΄ μμΌλ©°, λΌλ²¨μ κΈ°μ€μ λ¬Έμ₯μ κ°μ μΌλ‘ λΆλ₯νμ¬ μΌμ, λΆμ , κΈμ μΌλ‘ λλμμ΅λλ€.<br><br><br>
  </h6>
  <p>
</details>
<details>
<summary><b>λͺ¨λΈ νμ΅</b></summary>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/o5VYftQBrI.png">
</div>
  <h5> λͺ¨λΈ νμ΅ κ³Όμ  </h5>
  <h6> νμ΅μ max_epochs=15λ‘ 15λ² λ°λ³΅νμ¬ Train_lossκ°μ΄ κ°μ₯ λ?μ λͺ¨λΈμ μ μ₯νλ λ°©μμΌλ‘ μ§νλ©λλ€.<br><br>
       λ°μ΄ν°μ, λΌλ²¨μ μ, max_len μ΄ 3κ°μ§λ₯Ό μμ νμ¬ 3ν μ λ λͺ¨λΈ νμ΅μ μ§ννμμ΅λλ€. <br><br>
       μ΅μ’μ μΌλ‘ μ¬μ©ν λͺ¨λΈμ λ°μ΄ν°λ μ½ 236,000κ° / λΌλ²¨ μ΄ 3κ° / max_len = 64μ΄λ©°, epochs=4μΌ λ, Train_lossκ° 31.63μΌλ‘ κ°μ₯ λ?κ² λμμ΅λλ€. <br><br>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/ZjI4VldVdJ.png">
</div>
  <br><br><br>
  </h6>
  
</div>
</details>
<details>
<summary><b>μκ³ λ¦¬μ¦</b></summary>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/lY4MTWLTed.png">
</div>
</details>

<h2> π₯ νμ¬ λ° λμ κ°μ§ </h2>
 

<details>
<summary><b>νκ²½ λ° λ°μ΄ν°μ</b></summary>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/a2kd3yvFF0.png">
</div>
  <h5>κ΅¬μΆ νκ²½ </h5>
  <h6>Python 3.8 / Google Colab </h6>
  <h5>λ°μ΄ν°μ</h5>
  <h6>Yoloμ λ°μ΄ν°μμ <'AI HUB' νμ¬ λ°μ μμΈ‘ μμ>, <'GitHub' Fire-detection dataset>, <'AI HUB' μλμ΄ μ΄μνλ μμ>, <'Kaggle' Fall Detection Dataset> μ΄ 4κ°μ§λ₯Ό ν       μ©νμ¬ λ°μ΄ν°μμ κ΅¬μ±νμ΅λλ€.<br><br>
      λ°μ΄ν°μμ μ΄λ―Έμ§μ λΌλ²¨λ§ λ°μ΄ν° νμμΌλ‘ κ΅¬μ±λμ΄ μμΌλ©°, λΌλ²¨λ§ λ°μ΄ν°λ Label, CenterX, CenterY, Width, Heightλ‘ κ΅¬μ±λμ΄ μλ Yolo TXT ννμ¬μΌ ν©λλ€. <br><br>
      ν΄λΉ λ°μ΄ν°μ κ΅¬μ±μ μν΄ COCO Json to Yolo Txtκ³Ό XMLμ μ¬μ©νμ¬ λ‘λ³΄νλ‘μ°λ‘ ν΄λΉ λΌλ²¨λ§ λ°μ΄ν°λ₯Ό λ§λλ λ°©μμ μ ννμ΅λλ€.<br><br>
      λΌλ²¨λ§μ μ μ¬ μν© κ°μ§λ₯Ό μν΄ μ΄ 13κ°λ‘ κ΅¬μ±λμ΄ μμΌλ©°, μ€μ  νμ¬ λ° λμ κ°μ§ λΌλ²¨μ 2κ°μλλ€.<br><br><br>
  </h6>
</details>

<details>
<summary><b>λͺ¨λΈ νμ΅</b></summary>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/XWOHrkqMgU.png">
</div>
  <h5>λͺ¨λΈ νμ΅ κ³Όμ  </h5>
  <h6> λͺ¨λΈ νμ΅ λ°©μμ Pre-Trained Model νμΌμ νμΈνλ νλ λ°©μμΌλ‘ μ§ννμ΅λλ€. <br><br>
       ν΄λΉ νλ‘μ νΈλ μ€μκ° κ°μ§λ₯Ό λͺ©μ μΌλ‘ νκΈ° λλ¬Έμ v5s λͺ¨λΈμ μ ννμ¬ νμΈνλμ μ§ννμ΅λλ€. <br><br>
       batch-size=64, epochs=100 λ‘ νμ΅μ μ§ννμμΌλ©°,<br><br>
       epochs=84μΌ λ κ°μ₯ μ’μ λͺ¨λΈμ΄ μμ±λμμΌλ©°, 'metric/mAP_0.5:0.95' κ°μ΄ 0.619λ‘ 100λ²μ νμ΅ κ³Όμ λμ κ°μ₯ λκ² λμμ΅λλ€.<br><br>
       μ΅μ’ νμ΅μ΄ μ’λ£λ ν λμ¨ κ²°κ³Όκ°μ λ€μκ³Ό κ°μ΅λλ€.<br><br>

<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/5QFgM6YsBY.png">
</div>
  <br><br><br>
  </h6>
</details>

<details>
<summary><b>μκ³ λ¦¬μ¦</b></summary>
<div align= "center">
  <img width="850" src = "https://i.esdrop.com/d/f/CcSudjZ5R8/QgditBmOf1.png">
</div>
</details>

- - -
<div align = "center">
<h4> π½Tech Stack π½ </h4>
π Plaforms & Languages π¬
<br><br>
<img src = "https://img.shields.io/static/v1?label=Python&message=v3.8&color=red">
<img src = "https://img.shields.io/static/v1?label=Flask&message=2.2.2&color=orange">
<img src = "https://img.shields.io/static/v1?label=Matplotlib&message=3.5.3&color=yellow">
<br>
<img src = "https://img.shields.io/static/v1?label=Numpy&message=1.21.6&color=green">
<img src = "https://img.shields.io/static/v1?label=Opencv-python&message=4.7.0.68&color=blue">
<img src = "https://img.shields.io/static/v1?label=Pandas&message=1.3.5&color=navy">
<img src = "https://img.shields.io/static/v1?label=Torch&message=1.13.1&color=purple">
<br>
<img src = "https://img.shields.io/static/v1?label=&message=HTML&color=brightgreen">
<img src = "https://img.shields.io/static/v1?label=&message=JavaScript&color=coral">
</div>
