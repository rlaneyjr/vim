Vim�UnDo� #�#�K��ه�,Y��S��}�Nڐ�Nw�q�g�  Q   J    content_object = models.GenericForeignKey("content_type", "object_id")   �                          X>�    _�                     �       ����                                                                                                                                                                                                                                                                                                                            �          �          v       X;��     �   �   �  Q      K    content_object = generic.GenericForeignKey("content_type", "object_id")5�_�                       :    ����                                                                                                                                                                                                                                                                                                                            �          �   ,       v   ,    X;��     �        Q      :from django.contrib.contenttypes.models import ContentType5�_�                       ;    ����                                                                                                                                                                                                                                                                                                                            �          �   ,       v   ,    X;��     �        Q      <from django.contrib.contenttypes.models import ContentType, �        Q    5�_�                            ����                                                                                                                                                                                                                                                                                                                            �          �   ,       v   ,    X;��     �        Q      /from django.contrib.contenttypes import generic5�_�                       <    ����                                                                                                                                                                                                                                                                                                                               L          <       v   <    X;�D     �        Q      Mfrom django.contrib.contenttypes.models import ContentType, GenericForeignKey5�_�                       )    ����                                                                                                                                                                                                                                                                                                                               /          )       v   )    X;�L     �        Q      0#from django.contrib.contenttypes import generic�        Q    5�_�      	                 !    ����                                                                                                                                                                                                                                                                                                                               )          9       v   )    X;�U     �        Q      :#from django.contrib.contenttypes import GenericForeignKey5�_�      
          	      :    ����                                                                                                                                                                                                                                                                                                                               :                 v       X;�b     �        Q      <from django.contrib.contenttypes.models import ContentType, 5�_�   	              
      :    ����                                                                                                                                                                                                                                                                                                                               :                 v       X;�b     �        Q      ;from django.contrib.contenttypes.models import ContentType 5�_�   
                         ����                                                                                                                                                                                                                                                                                                                               :                 v       X;�e     �        Q      A#from django.contrib.contenttypes.fields import GenericForeignKey5�_�                            ����                                                                                                                                                                                                                                                                                                                              :                 v       X;�g    �  <  >              �  6  8              �  1  3                  �  &  (                      �  $  &          .            self.article.current_revision and �  "  $          +            not self.previous_revision and �    !              �              ?        convenient. Remember to always call this method before �                  �                  �  
            >    # Allow a revision to redirect to another *article*. This �    
              �              O    title = models.CharField(max_length=512, verbose_name=_(u'article title'), �                  �                   �   �   �              �   �   �              �   �   �              �   �   �              �   �   �              �   �   �              �   �   �              �   �   �              �   �   �          M    """This is an abstract model used as a mixin: Do not override any of the �   �   �              �   �   �              �   �   �              �   �   �              �   �   �              �   �   �                  �   �   �              �   �   �              �   �   �              �   �   �              �   �   �              �   �   �              �   �   �              �   �   �              �   }                 �   o   q          Q        assert self.id or save, ('Article.add_revision: Sorry, you cannot add a' �   i   k              �   ]   _              �   E   G              �   9   ;              �   -   /              �   (   *              �   #   %              �                    �                ?    current_revision = models.OneToOneField('ArticleRevision', �                    �                    5�_�                     �       ����                                                                                                                                                                                                                                                                                                                            �          �          v       X>�    �   �   �  Q      J    content_object = models.GenericForeignKey("content_type", "object_id")5�_�              	         :    ����                                                                                                                                                                                                                                                                                                                               :          ;       v       X;�^     �        Q      yfrom django.contrib.contenttypes.models import ContentTyperom django.contrib.contenttypes.fields import GenericForeignKey5��