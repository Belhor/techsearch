personal_refinments = '''<form>
						    <fieldset>
						       <legend>Personal Refinments</legend>

						       <fieldset> 
						             <legend>Search Scope</legend>
						          <div class="row hide-for-small">
						             <div class="small-12 columns">
						             	<div class="row">
						             	   <div class="small-1 columns">
						             	      <input type="radio" name="search_scope">
						             	   </div>
						             	   <div class="small-11 columns">
						             	      <label class="left">International</label>
						             	   </div>
						             	</div>
						             	<div class="row">
						             	   <div class="small-1 columns">
						             	      <input type="radio" name="search_scope">
						             	   </div>
						             	   <div class="small-11 columns">
						             	      <label class="left">USA</label>
						             	   </div>
						             	</div>
						             	<div class="row">
						             	   <div class="small-1 columns">
						             	      <input type="radio" name="search_scope">
						             	   </div>
						             	   <div class="small-11 columns">
						             	      <label class="left">UK</label>
						             	   </div>
						             	</div>
						             	</div>
						             </div>
						             <div class="row show-for-small">
						                <div class="small-12 columns">
						                	<select name="search-scope-select">
						                		<option value="International" selected>International</option>
						                		<option value="USA">USA</option>
						                		<option value="UK">UK</option>
						                	</select>
						                </div>
						             </div>					        
						       </fieldset>
						       <fieldset>
						          <legend>Price Range</legend>
						          <div class="row">
						             <div class="small-3 columns">
						                <label class="right">From:</label>						             
						             </div>
						             <div class="small-3 columns">
						                <input type="text" maxlength="100000">
						             </div>
						             <div class="small-3 columns">
						                <label class="right">To:</label>						             
						             </div>
						             <div class="small-3 columns">
						                <input type="text" maxlength="100000">
						             </div>

						         </div>
						       </fieldset>

						       <fieldset>
						          <legend>Condition</legend>
						          <div class="row">
						             <div class="small-2 columns">
						                <input type="radio" name="condition">
						             </div>
						             <div class="small-10 columns">
						                <label class="left">New</label>						             
						             </div>
						         </div>
						         <div class="row">
						             <div class="small-2 columns">
						                <input type="radio" name="condition">
						             </div>
						             <div class="small-10 columns">
						                <label class="left">Used</label>						             
						             </div>
						         </div>
						       </fieldset>

						       </fieldset>'''

motherboard_form = '''
                      <fieldset>
                               <legend>General Refinments</legend>
                                  <fieldset>
                                  	<legend>Brand</legend>
                                  	<div class="row">
						             	   <div class="small-2 columns">
						             	      <input type="radio" name="brand">
						             	   </div>
						             	   <div class="small-10 columns">
						             	      <label class="left">AMD</label>
						             	   </div>
						            </div>

						            <div class="row">
						             	   <div class="small-2 columns">
						             	      <input type="radio" name="brand">
						             	   </div>
						             	   <div class="small-10 columns">
						             	      <label class="left">Intel</label>
						             	   </div>
						            </div>

						            <div class="row">
						             	   <div class="small-2 columns">
						             	      <input type="radio" name="brand">
						             	   </div>
						             	   <div class="small-10 columns">
						             	      <label class="left">Asus</label>
						             	   </div>
						            </div>

						            <div class="row">
						             	   <div class="small-2 columns">
						             	      <input type="radio" name="brand">
						             	   </div>
						             	   <div class="small-10 columns">
						             	      <label class="left">Dell</label>
						             	   </div>
						            </div>

						            <div class="row">
						             	   <div class="small-2 columns">
						             	      <input type="radio" name="brand">
						             	   </div>
						             	   <div class="small-10 columns">
						             	      <label class="left">Gigabyte</label>
						             	   </div>
						            </div>

						            <div class="row">
						             	   <div class="small-2 columns">
						             	      <input type="radio" name="brand">
						             	   </div>
						             	   <div class="small-10 columns">
						             	      <label class="left">HP</label>
						             	   </div>
						            </div>

						            <div class="row">
						             	   <div class="small-2 columns">
						             	      <input type="radio" name="brand">
						             	   </div>
						             	   <div class="small-10 columns">
						             	      <label class="left">IBM</label>
						             	   </div>
						            </div>

						            <div class="row">
						             	   <div class="small-2 columns">
						             	      <input type="radio" name="brand">
						             	   </div>
						             	   <div class="small-10 columns">
						             	      <label class="left">Nvidia</label>
						             	   </div>
						            </div>

                                  </fieldset>

                                  <fieldset>
                                  <legend>Form Factor</legend>
                                  <div class="row">
						             	   <div class="small-2 columns">
						             	      <input type="radio" name="form_factor">
						             	   </div>
						             	   <div class="small-10 columns">
						             	      <label class="left">AT</label>
						             	   </div>
						          </div>

						          <div class="row">
						             	   <div class="small-2 columns">
						             	      <input type="radio" name="form_factor">
						             	   </div>
						             	   <div class="small-10 columns">
						             	      <label class="left">ATX</label>
						             	   </div>
						          </div>

						          <div class="row">
						             	   <div class="small-2 columns">
						             	      <input type="radio" name="form_factor">
						             	   </div>
						             	   <div class="small-10 columns">
						             	      <label class="left">BTX</label>
						             	   </div>
						          </div>

						          <div class="row">
						             	   <div class="small-2 columns">
						             	      <input type="radio" name="form_factor">
						             	   </div>
						             	   <div class="small-10 columns">
						             	      <label class="left">Extended ATX</label>
						             	   </div>
						          </div>

						          <div class="row">
						             	   <div class="small-2 columns">
						             	      <input type="radio" name="form_factor">
						             	   </div>
						             	   <div class="small-10 columns">
						             	      <label class="left">MicroATX</label>
						             	   </div>
						          </div>


                                  </fieldset>

                                  <fieldset>
						          <legend>Socket Type</legend>
						          <div class="row">
						             <div class="small-2 columns">
						                <input type="radio" name="socket_type">
						             </div>
						             <div class="small-10 columns">
						                <label class="left">LGA 1155/Socket H2</label>						             
						             </div>
						         </div>
						         <div class="row">
						             <div class="small-2 columns">
						                <input type="radio" name="socket_type">
						             </div>
						             <div class="small-10 columns">
						                <label class="left">LGA 1366/Socket B</label>						             
						             </div>
						         </div>
						         <div class="row">
						             <div class="small-2 columns">
						                <input type="radio" name="socket_type">
						             </div>
						             <div class="small-10 columns">
						                <label class="left">LGA 775/Socket T</label>						             
						             </div>
						         </div>

						       </fieldset>
						       <div class="row">
						          <div class="small-12 columns">
						             <input class="large button expand" type="submit" name="retrieve_list" value="Search">
						          </div>
						       </div>

                      </fieldset>

                       </form>'''